import os
from decouple import config # type: ignore

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage # type: ignore
from langchain_openai import ChatOpenAI # type: ignore

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-4o'
)

question = input('O que deseja saber? ')

messages = [
    SystemMessage(content='Você é um assistente que fornece informações sobre figuras históricas.'),
    HumanMessage(content=question),
    AIMessage(content='')
]

response = model.invoke(messages)

print(response)
print(response.content)