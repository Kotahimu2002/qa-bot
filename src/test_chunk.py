from ingest import extract_pdf_text, chunk_text

text = extract_pdf_text("data/report.pdf")

chunks = chunk_text(text)

print("Total Chunks:", len(chunks))

print("\nFirst Chunk:\n")
print(chunks[0])