import pinecone
import openai
from dotenv import load_dotenv
import os

_=load_dotenv()


pinecone.init(
    api_key = os.getenv("Pinecone_Key"),
    environment='gcp-starter'
    )
index = pinecone.Index('practice-index')
openai.api_key = os.getenv("OpenAI_Key")
