from ingest import load_and_split_pdf,load_and_split_url,load_and_split_docx,load_and_split_txt ,embedd_and_store
from query import retrive_documents, context_docs, generate_answer

input_data=["https://docs.cloud.google.com/dataform/docs/overview"]

if __name__ == "__main__":
    docs = load_and_split_url(input_data)
    print(f"Number of document chunks: {len(docs)}")
    for i, doc in enumerate(docs): 
        print(f"\n--- Document Chunk {i+1} ---\n{doc.page_content}\n")

    vector_store = embedd_and_store(docs)
    print("Vector store created and saved to data/faiss_index")
    print(f"Number of vectors in the store: {vector_store.index.ntotal}")   
    print(f"Vector store index path: data/faiss_index")
    
    query = input("Enter the query :")
    retrive_docs = retrive_documents(query, vector_store, k=20)
    context = context_docs(retrive_docs)
    answer = generate_answer(query, context)
    print("Answer :", answer)