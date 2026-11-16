import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

print("Starting AI Study Assistant...", flush=True)

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check your .env file.")

print("API key loaded successfully.", flush=True)

llm = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash",
    google_api_key=api_key,
    temperature=0.3,
    timeout=120,
    max_retries=1
)

prompt = ChatPromptTemplate.from_template("""
You are an AI Study Assistant.
Explain topics in simple language.
Help students understand their subjects.

Question: {question}
Answer:
""")

chain = prompt | llm | StrOutputParser()

print("Chatbot is ready!", flush=True)

while True:
    question = input("\nYou: ").strip()

    if question.lower() == "exit":
        print("Thank you for using AI Study Assistant!")
        break

    if not question:
        continue

    print("Connecting to Gemini...", flush=True)

    try:
        answer = chain.invoke({"question": question})
        print("\nAI Assistant:", answer, flush=True)

    except Exception as e:
        print("\nERROR:", repr(e), flush=True)