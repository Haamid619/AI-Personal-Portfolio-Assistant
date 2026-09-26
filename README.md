
# 🤖 AI Personal Portfolio Assistant

An AI-powered personal portfolio chatbot built using **Retrieval-Augmented Generation (RAG)**. The application uses my resume as a knowledge base and allows users to ask questions about my education, technical skills, projects, and professional background.

The main goal of this project was to understand how **LLMs, embeddings, vector databases, retrieval, and RAG pipelines** work together in a practical application.

---

## 🚀 Features

- Ask questions about my professional background
- Retrieve relevant information from my resume
- Generate natural-language responses using an LLM
- Uses RAG to ground responses in the available knowledge base
- Reduces hallucinations by instructing the LLM to answer only using retrieved information
- Interactive chatbot interface built with Streamlit
- Persistent vector storage using ChromaDB

---

## 🧠 How It Works

The application follows a simple RAG pipeline:

```text
                Resume / Documents
                       │
                       ▼
                PDF Text Extraction
                       │
                       ▼
                    Chunking
                       │
                       ▼
                  ChromaDB
                Vector Database
                       │
                       │
User Question ─────────┤
                       ▼
                   Retrieval
                       │
                       ▼
             Relevant Context
                       │
                       ▼
                Gemini LLM
                       │
                       ▼
                Generated Answer
                       │
                       ▼
               Streamlit Interface
````

### RAG Process

1. The resume is loaded from the `data/` directory.
2. Text is extracted from the PDF using `pypdf`.
3. The extracted text is divided into smaller chunks.
4. The chunks are stored in ChromaDB.
5. When a user asks a question, relevant information is retrieved from the knowledge base.
6. The retrieved information is provided as context to the Gemini LLM.
7. Gemini generates a response based on the retrieved context.
8. The response is displayed through the Streamlit chatbot interface.

---

## 🛠️ Tech Stack

| Technology       | Purpose                         |
| ---------------- | ------------------------------- |
| Python           | Application development         |
| Google Gemini    | Large Language Model (LLM)      |
| Google GenAI SDK | Gemini API integration          |
| ChromaDB         | Vector database and retrieval   |
| pypdf            | PDF text extraction             |
| python-dotenv    | Environment variable management |
| Streamlit        | Web-based chatbot interface     |

---

## 📁 Project Structure

```text
AI-Personal-Portfolio-Assistant/
│
├── data/
│   └── resume.pdf
│
├── app.py
├── ingest.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
```

### File Description

**`app.py`**

Provides the Streamlit user interface and handles user interaction.

**`ingest.py`**

Extracts text from the PDF, splits it into chunks, and stores the information in ChromaDB.

**`rag.py`**

Handles document retrieval and communication with the Gemini LLM to generate answers.

**`data/resume.pdf`**

The knowledge source used by the RAG pipeline.

**`requirements.txt`**

Contains the Python dependencies required to run the project.

---

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/Haamid619/AI-Personal-Portfolio-Assistant.git
```

```bash
cd AI-Personal-Portfolio-Assistant
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

#### Windows PowerShell

```powershell
.\venv\Scripts\Activate.ps1
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure the Gemini API key

Create a `.env` file in the project root:

```text
GEMINI_API_KEY=your_api_key_here
```

The `.env` file should **never be committed to GitHub**.

---

## 📚 Build the Knowledge Base

Run:

```bash
python ingest.py
```

This extracts the text from the resume and stores the resulting chunks in ChromaDB.

---

## ▶️ Run the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

---

## 💬 Example Questions

You can ask questions such as:

```text
What are my technical skills?
```

```text
What is my educational background?
```

```text
Tell me about my projects.
```

```text
What machine learning technologies do I know?
```

```text
What certifications do I have?
```

The system is also instructed to avoid inventing information that is not available in the knowledge base.

For example:

```text
What is my experience at Microsoft?
```

If that information is not present in the knowledge base, the assistant responds:

```text
I don't have that information in my portfolio.
```

---

## 🔍 Why RAG?

A traditional LLM can generate answers based on its pre-trained knowledge, but it does not automatically know the latest or private information about a specific person.

Instead of putting all information directly into every prompt, RAG allows the application to:

```text
Question
   ↓
Retrieve relevant information
   ↓
Provide retrieved information as context
   ↓
LLM generates the response
```

This makes it possible to connect a general-purpose LLM with a custom knowledge base.

It also allows the knowledge base to be updated without retraining the LLM.

---

## 🧩 Role of the LLM

This project uses **Google Gemini 2.5 Flash** as the Large Language Model.

The LLM is responsible for:

* Understanding the user's question
* Interpreting the retrieved context
* Following the instructions in the prompt
* Generating a natural-language response

The LLM itself was pre-trained by Google. This project does **not** train an LLM.

Instead, the project integrates the existing LLM into a custom RAG pipeline.

---

## 🔐 Security

The Gemini API key is stored in a `.env` file and excluded from version control using `.gitignore`.

Sensitive files such as:

```text
.env
venv/
chroma_db/
```

are not included in the repository.

---

## 🎯 Learning Objectives

This project was created primarily as a practical learning project to understand:

* Large Language Models (LLMs)
* LLM API integration
* Prompt engineering
* Retrieval-Augmented Generation (RAG)
* Document processing
* Text chunking
* Vector databases
* Semantic retrieval
* Context injection
* Hallucination reduction
* Streamlit application development

---

## 🔮 Future Improvements

Possible future improvements include:

* Adding additional project documents to the knowledge base
* Improving chunking with overlapping chunks
* Using explicit embedding models
* Displaying retrieved sources in the UI
* Adding conversation history
* Improving the chatbot interface
* Deploying the application online

---

## 👨‍💻 Author

**Syed Haamid Ali**

B.E. Electronics & Communication Engineering
HKBK College of Engineering, Bengaluru

### Connect

* GitHub: [https://github.com/Haamid619](https://github.com/Haamid619)
* LinkedIn: [https://linkedin.com/in/haamidalI619](https://linkedin.com/in/haamidalI619)

---

## 📄 License

This project is intended primarily as a personal learning and portfolio project.

````

### One small correction before you paste it

Your LinkedIn URL should use your actual profile URL. In the README above, I wrote:

```text
https://linkedin.com/in/haamidalI619
````

The last character there can easily be confused between lowercase **l** and uppercase **I**. **Use the exact URL from your LinkedIn profile** rather than copying that line blindly.

Also, because you're putting your **resume on a public GitHub repository**, check whether you're comfortable exposing your email/phone/contact information publicly. If not, use a sanitized version of the resume for the repository.

Available next action: Create a downloadable DOCX file here in this chat containing the editable prose above
