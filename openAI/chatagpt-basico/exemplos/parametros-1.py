from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()
cliente = OpenAI()

resposta = cliente.chat.completions.create(
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
    # max_tokens = 20
    # stop=['?', '\n']
    n=3
)

for escolha in resposta.choices:
    print(escolha.message.content)
    print('='*50)