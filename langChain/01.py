import os
from decouple import config # type: ignore

from langchain_openai import OpenAI # type: ignore

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

model = OpenAI()

question = input('O que você deseja saber hoje?')

response = model.invoke(
    input=question,
)

print(response)