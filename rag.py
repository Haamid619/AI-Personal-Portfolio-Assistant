import os

import chromadb
from dotenv import load_dotenv
from google import genai


# Load API key
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("GEMINI_API_KEY was not found in .env")


# Create Gemini client
gemini_client = genai.Client(
    api_key=API_KEY
)


# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="chroma_db"
)

collection = client.get_collection(
    name="portfolio"
)


def search_documents(question, n_results=1):

    results = collection.query(
        query_texts=[question],
        n_results=n_results
    )

    return results["documents"][0]


def generate_answer(question):

    # Retrieve relevant information
    relevant_documents = search_documents(question)

    # Combine retrieved information
    context = "\n\n".join(relevant_documents)

    # Prompt
    prompt = f"""
You are an AI assistant representing Syed Haamid Ali.

Answer the user's question using ONLY the information
provided in the context below.

If the answer is not available in the context, say:

"I don't have that information in my portfolio."

Do not invent qualifications, experience, projects,
technologies, companies, or achievements.

Keep your answer concise and professional.

CONTEXT:
{context}

USER QUESTION:
{question}

ANSWER:
"""

    # Generate response using Gemini
    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text


# Test from terminal
if __name__ == "__main__":

    question = input("Ask a question about the portfolio: ")

    answer = generate_answer(question)

    print("\nAI Answer:\n")
    print(answer)