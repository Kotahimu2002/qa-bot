from ingest import extract_pdf_text

text = extract_pdf_text("data/report.pdf")

print(text[:1000])