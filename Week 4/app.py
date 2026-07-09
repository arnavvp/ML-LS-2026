import streamlit as st

from src.rag import answer_question


st.set_page_config(
    page_title="IITB Insti-Assist",
    page_icon="🎓"
)


st.title("🎓 IITB Insti-Assist")


st.write(
    """
    Ask questions about IIT Bombay academics,
    rules, policies and procedures.
    """
)


question = st.text_input(
    "Ask a question:"
)


if question:

    with st.spinner(
        "Searching relevant documents..."
    ):
        answer, chunks, confidence, grounded = answer_question(question)


    st.subheader("Answer")

    st.write(answer)
    st.subheader("Grounding Confidence")
    st.write(grounded)
    st.progress(min(confidence, 1.0))
    st.write("Similarity Score:",round(confidence, 3))
    st.subheader("Retrieved Evidence")

    for chunk in chunks:

        with st.expander("📄 " + chunk["source"]):

            st.write(chunk["text"])

            st.write("Retrieval Score:",round(chunk["score"], 3))