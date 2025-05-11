# 📊 Streamlit Chatbot for Financial Report Analysis (Apple 10-Q RAG)

This is an interactive, LLM-powered chatbot built with Streamlit and LangChain. It allows users to ask questions over Apple's 10-Q earnings reports and get precise, grounded answers using vector search (FAISS) and OpenAI's GPT-3.5.

---

## 🔧 What This Project Demonstrates

- Retrieval-Augmented Generation (RAG) architecture using LangChain
- HuggingFace embeddings + FAISS vector database for semantic search
- Conversational memory using GPT-3.5 via OpenAI
- Fully deployed Streamlit UI with clean modular code
- Real-world use case: Q&A over Apple’s Q2 10-Q Management Discussion section

---

## 🚀 How to Run Locally

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set OpenAI API Key

Create a `.env` file:

```bash
echo "OPENAI_API_KEY=your-key-here" > .env
```

Or export in terminal:

```bash
export OPENAI_API_KEY=your-key-here
```

### 3. Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
apple-10q-rag-chatbot/
├── app.py
├── requirements.txt
├── .gitignore
├── README.md
└── faiss_index/
    ├── index.faiss
    └── index.pkl  # <- Not committed to GitHub
```

---

## 📌 Use Case

This chatbot demonstrates how financial analysts, auditors, or curious users can query 10-Q filings and extract insights such as:

- What impacted Apple’s earnings in Q2 2025?
- What macroeconomic risks were disclosed?
- How did Apple’s performance compare YoY across segments?

---

## 🌐 Deployment (Optional)

If you want to deploy this app:
- Push to GitHub
- Connect to [Streamlit Cloud](https://streamlit.io/cloud)
- Set `OPENAI_API_KEY` in secrets

---

## 🛠️ Future Direction

This was a foundational project to validate LLM + retrieval use cases. The architecture will be extended in a separate repo with other projects.
