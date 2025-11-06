import os
from dotenv import load_dotenv
from typing import List
from langchain_community.document_loaders import PyPDFLoader,WebBaseLoader,Docx2txtLoader,TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

    # Load environment variables from .env file
load_dotenv()

    # Split the document into smaller chunks
splitter = RecursiveCharacterTextSplitter(chunk_size=700, chunk_overlap=150)

    # Load the PDF document
def load_and_split_pdf(input_file_path):
    
    loader = PyPDFLoader(input_file_path)
    docs = loader.load()
    return splitter.split_documents(docs)

    # Filter out empty strings if user left some URL boxes blank
def load_and_split_url(input_data: list[str]):

    input_data = [u for u in input_data if u]
    loader = WebBaseLoader(input_data)
    docs = loader.load()
    return splitter.split_documents(docs)

    # load docx
def load_and_split_docx(input_file_path):
    
    loader = Docx2txtLoader(input_file_path)
    docs = loader.load()
    return splitter.split_documents(docs)

def load_and_split_txt(input_file_path):
    loader = TextLoader(input_file_path)
    docs = loader.load()
    return splitter.split_documents(docs)


    # Create embeddings and store in FAISS vector store    
def embedd_and_store(docs):
    # Create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="BAAI/bge-large-en-v1.5") #text-embedding-3-large

    # Create a FAISS vector store from the document chunks
    vector_store = FAISS.from_documents(docs, embeddings)

    os.makedirs("data/faiss_index", exist_ok=True)

    # Save the vector store to disk
    vector_store.save_local("data/faiss_index")

    return vector_store   