from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import OpenAI


load_dotenv()

llm = OpenAI()

response = llm.invoke("Hello there my name is john...")

print(response)