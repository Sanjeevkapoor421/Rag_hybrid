
from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

def retrive_documents(query, vector_store, k = 20):
    # Retrieve relevant documents based on the query
    return vector_store.similarity_search(query, k=k)
    
def context_docs(retrive_docs):
    # Extract and return the content of the retrieved documents
    context = "\n".join([doc.page_content for doc in retrive_docs])
    return context

def generate_answer(query,context):
    # Initialize the ChatOpenAI model
    llm = ChatOpenAI(model="gpt-4.1", temperature=0)

    prompt = ChatPromptTemplate.from_messages([
             ("system",
              "You are a precise assistant. Use ONLY the provided context to answer. "
              "If the answer is not in the context, say \"I don't know.\""),
              ("human", "Context: {context}\n\nQuestion: {question}:")]
    )

    # Generate an answer using the LLM
    messages = prompt.format_messages(question=query, context=context)
    Answer = llm.invoke(messages)
    return Answer.content
