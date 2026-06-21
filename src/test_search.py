import chromadb

client = chromadb.PersistentClient(path="db")

collection = client.get_collection(
    name="document_chunks"
)

results = collection.query(
    query_texts=["What is this document about?"],
    n_results=2
)

print(results["documents"])