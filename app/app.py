import os
import streamlit as st
import shutil
from langchain_community.vectorstores import FAISS
from ingest import load_and_split_pdf,load_and_split_url,load_and_split_docx,load_and_split_txt ,embedd_and_store
from query import retrive_documents, context_docs, generate_answer

def processing_input(input_type, input_data):   

    if input_type == "PDF":
        if not input_data:
            st.error("Please upload a PDF file first.")
        st.write("Processing the input file and creating vector store...")
        docs = load_and_split_pdf(input_data) 

    elif input_type == "Link":
        if not input_data or all(not url for url in input_data):
            st.error("Please enter at least one URL.")
        st.write("Processing the input URLs and creating vector store...")
        docs = load_and_split_url(input_data)

    elif input_type == "DOCX":
        if not input_data:
            st.error("Please upload a DOCX file first.")
        st.write("Processing the input file and creating vector store...")
        docs = load_and_split_docx(input_data)

    elif input_type == "TXT":
        if not input_data:
            st.error("Please upload a TXT file first.")
        st.write("Processing the input file and creating vector store...")
        docs = load_and_split_txt(input_data)    

        # to process the input file and create vector store
    vector_store = embedd_and_store(docs)
    
    
    return vector_store

def cleanup_temp_files():
    temp_folders = ["data/input_pdf", "data/faiss_index", "data/input_docx", "data/input_txt"]
    for folder in temp_folders:
        if os.path.exists(folder):
            shutil.rmtree(folder)
            print(f"🧹 Cleared {folder}")        

def main():
    st.title("Hello😊! Welcome to my RAG Chat💬")
    st.write("This is a simple RAG application using Streamlit.")
    input_type = st.selectbox("Input Type", ["Link", "PDF", "DOCX", "TXT"])

    input_data = None 

    # to handle Link input

    if input_type == "Link":
        number_input = st.number_input(min_value=1, max_value=20, step=1, label = "Enter the number of Links")
        input_data = []
        for i in range(number_input):
            url = st.sidebar.text_input(f"URL {i+1}")
            input_data.append(url)

    # to handle PDF file upload

    elif input_type == "PDF":
        input_data = st.file_uploader("Upload a PDF file", type=["pdf"])
        if input_data is None:
            st.warning("Please upload a PDF file to proceed.")
            return
        os.makedirs("data/input_pdf/", exist_ok=True)
        pdf_path = "data/input_pdf/"
        input_file_path = os.path.join(pdf_path, input_data.name)
        with open(input_file_path, "wb") as f:
                f.write(input_data.read())

        if input_file_path is not None:
            st.write("File uploaded successfully.") 
        input_data = input_file_path    

     # to handle DOCX file upload
     #         
    elif input_type in ["DOCX"]:
        input_data = st.file_uploader("Upload a DOCX file", type=["docx"])
        if input_data is None:
            st.warning("Please upload a DOCX file to proceed.")
            return
        os.makedirs("data/input_docx/", exist_ok=True)
        docx_path = "data/input_docx/"
        input_file_path = os.path.join(docx_path, input_data.name)
        with open(input_file_path, "wb") as f:
                f.write(input_data.read())

        if input_file_path is not None:
            st.write("File uploaded successfully.")
        input_data = input_file_path    

    elif input_type == "TXT":
        input_data = st.file_uploader("Upload a TXT file", type=["txt"])
        if input_data is None:
            st.warning("Please upload a TXT file to proceed.")
            return
        os.makedirs("data/input_txt/", exist_ok=True)
        txt_path = "data/input_txt/"
        input_file_path = os.path.join(txt_path, input_data.name)
        with open(input_file_path, "wb") as f:
                f.write(input_data.read())  
        if input_file_path is not None:
            st.write("File uploaded successfully.")  
        input_data = input_file_path    


    if st.button("Proceed"):
         st.write("Creating vector store, please wait...")
         vector_store = processing_input(input_type,input_data)
         st.write("your documents are uploaded successfully!, please end the session after your query")   
         st.session_state['vector_store'] = vector_store
        # to handle query and get answer
    if "vector_store" in st.session_state:

        query = st.text_input("Enter your query:")

        if st.button("Submit"):
            retrive_docs = retrive_documents(query, st.session_state["vector_store"], k=8)
            context = context_docs(retrive_docs)
            answer = generate_answer(query, context)
            st.write("Answer :", answer)

    if st.button("End Session"):
        cleanup_temp_files()
        st.session_state.clear()
        st.success("Session ended and temporary files cleared ✅")        
        
if __name__ == "__main__":
    main()