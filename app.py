import streamlit as st
from dotenv import load_dotenv
import os

# ✅ Must be first Streamlit command
st.set_page_config(page_title="RAG Chatbot", layout="wide")

# ✅ Load environment variables securely (e.g., OPENAI_API_KEY)
load_dotenv()

# LangChain & Vector Store Imports
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_huggingface import HuggingFaceEmbeddings

# ✅ Cache model + vectorstore loading for faster runs
@st.cache_resource
def setup_qa_chain():
    embedding = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local("faiss_index", embedding, allow_dangerous_deserialization=True)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True, output_key="answer")

    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=retriever,
        memory=memory,
        return_source_documents=True,
        output_key="answer"
    )
    return qa_chain

qa_chain = setup_qa_chain()

# ✅ Initialize chat history if empty
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title("📊 Apple 10-Q Analyst Bot")

# ✅ 1. Show chat history (messages appear in order)
for role, msg in st.session_state.chat_history:
    with st.chat_message(role):
        st.markdown(msg)

# ✅ 2. Input box appears at the bottom
def handle_user_input():
    user_question = st.session_state.input_box
    if user_question:
        response = qa_chain.invoke({"question": user_question})
        st.session_state.chat_history.append(("You", user_question))
        st.session_state.chat_history.append(("AI", response["answer"]))
        st.session_state.input_box = ""  # ✅ This now works, because it's called *before* rerender

# Input box with submission handler
st.text_input(
    "Ask your question:",
    key="input_box",
    on_change=handle_user_input
)

