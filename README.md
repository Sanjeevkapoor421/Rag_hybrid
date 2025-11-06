# 💬 RAG Chat Assistant
This project is developed as a hybrid RAG (Retrieval-Augmented Generation) system that allows you to chat with your own data sources — including PDF, Web Links, DOCX, and TXT files.
Built fully in Streamlit, it runs your entire RAG pipeline (data loading → embedding → FAISS indexing → context retrieval → answer generation).

# prerequisite
create .env file and add your api key. 

# ⚙️ Project Overview
* Framework: Streamlit (Python)
* Embeddings: BAAI/bge-large-en-v1.5 via langchain-huggingface
* Vector Store: FAISS (Local storage)
* LLM (Answer generation): Open-source model (Llama-3, Mistral-7B, or Phi-3-Mini)
* Features:
     * Upload multiple input formats (PDF / DOCX / TXT)
     * Web link ingestion using web loaders
     * Automatic document chunking and embedding
     * FAISS-based semantic retrieval
     * Clean Streamlit interface with session-based state
     * Offline open-source mode (no API keys)

# 🚀Run this project:

### 1) Clone this project to your local using the below git command 
    ```bash
    
    git clone https://github.com/Sanjeevkapoor421/Rag_hybrid.git
    cd Rag_hybrid
    
    ```
### 2) Do git checkout to developement_branch
    ```bash
    git checkout features/base
    ```
# 🛠️ Manually run this project

### 3) Create a python virtual env

## For mac users
    ```bash  
    python -m venv ragenv  
    source ragenv/bin/activate
    ```
## For windows users   
    ```bash  
    python -m venv ragenv  
    ragenv/Scripts/activate
    ``` 
### 4) Install the requirements
    ```bash
    pip install -r requirements.txt
    ```
### 5) Run the project
    ```bash
    streamlit run app/app.py
    ``` 
This will :
 * create a virtual environment " myenv " ✅
 * It will install the required dependencies from requirements file ✅
 * Launch the Streamlit web UI at http://localhost:8501 ✅
 * Happy Chatting with your PDFs, DOCX, TXT, or web links 💬 
