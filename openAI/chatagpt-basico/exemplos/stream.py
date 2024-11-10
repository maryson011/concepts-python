from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
import sys
import time

load_dotenv()
cliente = OpenAI()

stream = cliente.chat.completions.create(
    model='gpt-3.5-turbo', # 'gpt-4o' ou 'gpt-4o-mini' (nova versão)
    messages=[
        {
            'role': 'system',
            'content': 'Você é um assistente util'
        },
        {
            'role': 'user',
            'content': 'Me conte uma piada'
        }
    ],
    stream=True
)

for chunk in stream:
    conteudo = chunk.choices[0].delta.content
    if conteudo is not None:
        print(conteudo, end='')
        sys.stdout.flush()
        time.sleep(0.3)