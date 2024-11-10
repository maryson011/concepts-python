from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
import os

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
cliente = OpenAI(api_key=OPENAI_API_KEY)