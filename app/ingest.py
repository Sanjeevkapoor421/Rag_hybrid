import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chat_models import ChatOpenAI


pdf_path = os.path.join("../docs", "Abstract.pdf")

    # Load environment variables from .env file
load_dotenv()

def load_and_split_pdf(pdf_path):
    # Load the PDF document
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    # Split the document into smaller chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)

    return docs

def embedd_and_store(docs):
    # Create embeddings
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

    # Create a FAISS vector store from the document chunks
    vector_store = FAISS.from_documents(docs, embeddings)

    os.makedirs("data/faiss_index", exist_ok=True)

    # Save the vector store to disk
    vector_store.save_local("data/faiss_index")

    return vector_store
def retrive_documents(query, vector_store, k = 3):
    # Retrieve relevant documents based on the query
    retrive_docs = vector_store.similarity_search(query, k=k)
    return retrive_docs

def generate_answer(query, retrive_docs):
    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    # Create a prompt by combining the query with the retrieved documents
    context = "\n".join([doc.page_content for doc in retrive_docs])
    prompt = f"Context: {context}\n\nQuestion: {query}\nAnswer:"

    # Generate an answer using the LLM
    response = llm.predict(prompt)
    return response

    

if __name__ == "__main__":
    docs = load_and_split_pdf(pdf_path)
    print(f"Number of document chunks: {len(docs)}")
    for i, doc in enumerate(docs):  # Print first 3 chunks for verification
        print(f"\n--- Document Chunk {i+1} ---\n{doc.page_content}\n")

    vector_store = embedd_and_store(docs)
    print("Vector store created and saved to data/faiss_index")
    print(f"Number of vectors in the store: {vector_store.index.ntotal}")   
    print(f"Vector store index path: data/faiss_index")
    print(f"Vector store index files: {os.listdir('data/faiss_index')}")
    query = input("\nEnter your query: ")
    retrive_docs = retrive_documents(query, vector_store)
    print(f"Number of retrieved documents: {len(retrive_docs)}")
    for i, doc in enumerate(retrive_docs):  # Print retrieved documents for verification
        print(f"\n--- Retrieved Document {i+1} ---\n{doc.page_content}\n")
    answer = generate_answer(query, retrive_docs)
    print(f"\n--- Answer ---\n{answer}\n")

