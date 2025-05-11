# 📊 TaxBot: Apple 10-Q Analyst Chatbot

TaxBot is an interactive, LLM-powered chatbot built with Streamlit and LangChain. It allows users to ask questions over Apple's 10-Q earnings reports and get precise, grounded answers using vector search (FAISS) and OpenAI's GPT-3.5.

---

## 🔧 Features
- Conversational retrieval over earnings reports
- FAISS-based semantic search
- HuggingFace embeddings for chunk indexing
- Streamlit chat UI with memory and follow-ups

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set OpenAI API Key

Create a `.env` file:

```bash
echo "OPENAI_API_KEY=your-key-here" > .env
```

Or set in terminal before launch:

```bash
export OPENAI_API_KEY=your-key-here
```

### 3. Run the App

```bash
streamlit run app.py
```

---

## 📁 Project Structure

```
taxbot_project/
├── app.py
├── requirements.txt
├── .env               # Not tracked in Git
├── .gitignore
├── README.md
└── faiss_index/
    ├── index.faiss
    └── index.pkl
```

---

## ☁️ Deployment

This app can be deployed via:
- [Streamlit Cloud](https://streamlit.io/cloud)
- GitHub Codespaces
- Self-hosted server with Python 3.10+
