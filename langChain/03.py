import os
from decouple import config # type: ignore

from langchain.prompts import ChatPromptTemplate, HumanMessagePromptTemplate # type: ignore
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage # type: ignore
from langchain_openai import ChatOpenAI # type: ignore

os.environ['OPENAI_API_KEY'] = config('OPENAI_API_KEY')

model = ChatOpenAI(
    model='gpt-4o'
)

chat_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content='Você deve responder baseado em dados geográficos de regiões do Brasil.'
        ),
        HumanMessagePromptTemplate.from_template(
            template='Por favor, me fale sobre a região {regiao}.'
        ),
        AIMessage(
            content='Claro, vou começar coletanto informações sobre a região e analisando os dados disponíveis.'
        ),
        HumanMessage(
            content='Certifique-se de incluir dados demográficos.'
        ),
        AIMessage(
            content='Entendido. Aqui estão os dados.'
        )
    ]
)

regiao = input('Sobre qual região deseja saber? ')

prompt = chat_template.format_messages(regiao=regiao)
# print(prompt)

response = model.invoke(prompt)
print(response)
print(response.content)