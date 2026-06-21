from ingest import extract_pdf_text, chunk_text
import chromadb

# Read PDF
text = extract_pdf_text("data/report.pdf")

# Create chunks
chunks = chunk_text(text)

# Create ChromaDB Client
client = chromadb.PersistentClient(path="db")

collection = client.get_or_create_collection(
    name="document_chunks"
)
try:
    client.delete_collection("document_chunks")
except:
    pass

collection = client.get_or_create_collection(
    name="document_chunks"
)

# Store chunks
for i, chunk in enumerate(chunks):
    collection.add(
        ids=[f"chunk_{i}"],
        documents=[chunk],
        metadatas=[
            {
                "source": "report.pdf",
                "chunk_number": i + 1
            }
        ]
    )

print(f"Stored {len(chunks)} chunks successfully!")