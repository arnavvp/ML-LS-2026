import streamlit as st
import io
import fitz
from src.rag import (
    answer_question,
    answer_with_chunks
)

from src.pdf_rag import (
    create_pdf_index,
    search_pdf
)


st.set_page_config(
    page_title="IITB Insti-Assist",
    page_icon="🎓"
)


st.title("🎓 IITB Insti-Assist")


st.write(
    """
    Ask questions about IIT Bombay academics,
    rules, policies and procedures.
    Upload a PDF to query your own documents.
    """
)


uploaded_pdf = st.file_uploader(
    "Upload your own PDF",
    type="pdf"
)


pdf_index = None
pdf_chunks = None


if uploaded_pdf:

    with st.spinner(
        "Processing PDF..."
    ):

        pdf_bytes = uploaded_pdf.getvalue()

        st.write("Filename:", uploaded_pdf.name)
        st.write("Size:", len(pdf_bytes))
        st.write("Header:", pdf_bytes[:20])


        doc = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in doc:
            text += page.get_text()


            pdf_index, pdf_chunks = create_pdf_index(
                    text,
                    uploaded_pdf.name
                )


    st.success(
        "PDF processed successfully!"
    )


question = st.text_input(
    "Ask a question:"
)


if question:

    with st.spinner(
        "Searching relevant documents..."
    ):


        if uploaded_pdf:

            chunks = search_pdf(
                question,
                pdf_index,
                pdf_chunks
            )


            answer, confidence = answer_with_chunks(
                question,
                chunks
            )


            grounded = "Uploaded PDF"


        else:

            answer, chunks, confidence, grounded = answer_question(
                question
            )


    st.subheader(
        "Answer"
    )

    st.write(
        answer
    )


    st.subheader(
        "Grounding Confidence"
    )


    st.write(
        grounded
    )


    st.progress(
        min(
            confidence,
            1.0
        )
    )


    st.write(
        "Similarity Score:",
        round(
            confidence,
            3
        )
    )


    st.subheader(
        "Retrieved Evidence"
    )


    for chunk in chunks:

        with st.expander(
            "📄 " + chunk["source"]
        ):

            st.write(
                chunk["text"]
            )


            st.write(
                "Retrieval Score:",
                round(
                    chunk["score"],
                    3
                )
            )