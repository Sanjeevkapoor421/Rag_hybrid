from dotenv import load_dotenv
import os
load_dotenv()

print("LangSmith tracing:", os.getenv("LANGCHAIN_TRACING_V2"))
print("LangSmith project:", os.getenv("LANGCHAIN_PROJECT"))
print("LangSmith endpoint:", os.getenv("LANGCHAIN_ENDPOINT"))
print("Has API key:", bool(os.getenv("LANGCHAIN_API_KEY")))