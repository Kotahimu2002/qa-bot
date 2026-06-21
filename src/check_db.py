import chromadb

client = chromadb.PersistentClient(path="db")

collection = client.get_collection("document_chunks")

data = collection.get()

print(data["metadatas"])