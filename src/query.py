import os
import chromadb
from google import genai
from dotenv import load_dotenv

load_dotenv()

# Gemini Client
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ChromaDB
chroma_client = chromadb.PersistentClient(path="db")

collection = chroma_client.get_collection(
    name="document_chunks"
)


def ask_question(question):

    # Retrieve relevant chunks
    results = collection.query(
    query_texts=[question],
    n_results=3,
    include=["documents", "metadatas"]
    )

    context_blocks = []


    for doc, meta in zip(
        results["documents"][0],
        results["metadatas"][0]
    ):
        source = "Unknown Source"

        if meta is not None:
            source = meta.get("source", "Unknown Source")

        context_blocks.append(
            f"[Source: {source}]\n{doc}"
        )

    context = "\n\n".join(context_blocks)

    prompt = f"""
You are a professional document Q&A assistant.

Answer ONLY using the provided context.

Mention source citations.

If answer is unavailable, say:

'I cannot find the answer in the provided document.'

Context:
{context}

Question:
{question}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text