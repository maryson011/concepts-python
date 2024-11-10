from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore

load_dotenv()
cliente = OpenAI()

resposta = cliente.chat.completions.create(
    model='gpt-3.5-turbo', # 'gpt-4o'
    messages=[
        {
            'role': 'system',
            'content': 'Você é um assistente util'
        },
        {
            'role': 'user',
            'content': 'Me conte uma piada'
        }
    ]
)
texto_resposta = resposta.choices[0].message.content
print(texto_resposta)