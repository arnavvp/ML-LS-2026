import os

import google.generativeai as genai

from dotenv import load_dotenv

from src.retriever import retrieve


load_dotenv()


genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)


model = genai.GenerativeModel(
   "gemini-2.5-flash-lite"
)



def answer_question(question):

    retrieved_chunks = retrieve(
        question,
        k=5
    )


    context = ""


    for i, chunk in enumerate(retrieved_chunks):

        context += f"""

SOURCE {i+1}: {chunk["source"]}

{chunk["text"]}

"""


    prompt = f"""
You are IITB Insti-Assist.

You answer questions about IIT Bombay using ONLY the provided context.

Rules:
- Do not use outside knowledge.
- If the answer cannot be reasonably inferred from the context, say exactly:
"I don't know based on the available IIT Bombay documents."
- Do not guess.
- Mention the source document used.

CONTEXT:
{context}


QUESTION:
{question}


ANSWER:
"""
    print("\n========== CONTEXT SENT ==========")

    for c in retrieved_chunks:
        print("\nSOURCE:", c["source"])
        print(c["text"][:500])

    print("==================================")

    response = model.generate_content(
        prompt
    )


    confidence = max(
        [
            chunk["score"]
            for chunk in retrieved_chunks
        ]
    )


    if confidence > 0.45:

        grounded = "Highly Grounded"

    elif confidence > 0.30:

        grounded = "Partially Grounded"

    else:

        grounded = "Low Confidence"


    return (
        response.text,
        retrieved_chunks,
        confidence,
        grounded
    )

def answer_with_chunks(question, retrieved_chunks):

    context = ""


    for chunk in retrieved_chunks:

        context += f"""

SOURCE: {chunk["source"]}

{chunk["text"]}

"""


    prompt = f"""
You are a document assistant.

Answer ONLY using this context.

If the answer is missing, say:
"I don't know based on the provided document."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""


    response = model.generate_content(
        prompt
    )


    confidence = max(
        chunk["score"]
        for chunk in retrieved_chunks
    )


    return (
        response.text,
        confidence
    )