from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv
import os

# Load your API key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Set up Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=api_key
)

# Message history
messages = [
    SystemMessage(content='You are a helpful assistant'),
    HumanMessage(content='Tell me about LangChain')
]

# Invoke Gemini with messages
try:
    result = model.invoke(messages)
    messages.append(AIMessage(content=result.content))
    print(messages)
except Exception as e:
    print("❌ Error:", e)
