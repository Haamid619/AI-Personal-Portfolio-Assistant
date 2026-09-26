import os
from pypdf import PdfReader
import chromadb


DATA_FOLDER = "data"
DB_FOLDER = "chroma_db"


# Create ChromaDB client
client = chromadb.PersistentClient(path=DB_FOLDER)

# Create collection
collection = client.get_or_create_collection(
    name="portfolio"
)


def extract_text_from_pdf(file_path):
    """Extract text from a PDF."""

    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def split_text(text, chunk_size=500):
    """Split text into smaller chunks."""

    words = text.split()

    chunks = []

    for i in range(0, len(words), chunk_size):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)

    return chunks


def ingest_documents():

    document_id = 0

    for filename in os.listdir(DATA_FOLDER):

        if not filename.lower().endswith(".pdf"):
            continue

        file_path = os.path.join(DATA_FOLDER, filename)

        print(f"Processing: {filename}")

        text = extract_text_from_pdf(file_path)

        if not text.strip():
            print(f"WARNING: No text found in {filename}")
            continue

        chunks = split_text(text)

        for chunk in chunks:

            collection.add(
                documents=[chunk],
                ids=[f"document_{document_id}"],
                metadatas=[
                    {
                        "source": filename
                    }
                ]
            )

            document_id += 1

    print(f"\nSuccessfully added {document_id} chunks.")


if __name__ == "__main__":
    ingest_documents()
    