# 💬 RAG Chat Assistant
This project is developed as a hybrid RAG (Retrieval-Augmented Generation) system that allows you to chat with your own data sources — including PDF, Web Links, DOCX, and TXT files.
Built fully in Streamlit, it runs your entire RAG pipeline (data loading → embedding → FAISS indexing → context retrieval → answer generation).

# prerequisite
create your api key and add it to .env file. 

# ⚙️ Project Overview
* Framework: Streamlit (Python)
* Embeddings: BAAI/bge-large-en-v1.5 via langchain-huggingface
* Vector Store: FAISS (Local storage)
* LLM (Answer generation): gpt-4.1
* Features:
     * Upload multiple input formats (PDF / DOCX / TXT)
     * Web link ingestion using web loaders
     * Automatic document chunking and embedding
     * FAISS-based semantic retrieval
     * Clean Streamlit interface with session-based state

# 🚀Run this project:

### 1) Clone this project to your local using the below git command 
    git clone https://github.com/Sanjeevkapoor421/Rag_chat.git
    cd Rag_chat
    
### 2) Do git checkout to developement_branch
    
    git checkout features/base

### 3) Automated run for mac or linux users
     make run    
    
### 4)Automated run for windows users  
     make -f app/Makefile run  

# 🛠️ Manually run this project

### 4) Create a python virtual env

## For mac users
     
    python3 -m venv ragenv  
    source ragenv/bin/activate

## For windows users   
    
    python3 -m venv ragenv  
    ragenv/Scripts/activate
    
### 4) Install the requirements
    
    pip install -r requirements.txt
    
### 5) Run the project
    
    streamlit run app/app.py
    
This will :
 * create a virtual environment " myenv " ✅
 * It will install the required dependencies from requirements file ✅
 * Launch the Streamlit web UI at http://localhost:8501 ✅
 * Happy Chatting with your PDFs, DOCX, TXT, or web links 💬 
