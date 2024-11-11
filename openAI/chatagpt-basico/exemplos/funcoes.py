from utils import cliente
import random
import json

historico = [
        {
            'role': 'system',
            'content': 'Você é um assistente util'
        },
        {
            'role': 'user',
            'content': 'Qual é a avaliação do filme Carros?'
        }
    ]

def enviar():
    desc_funcao = {
    'name': 'pegar_nota',
    'description': 'Obtem a nota de um filme',
    'parameters': {
        'type': 'object',
        'properties': {
            'titulo':{
                'type': 'string',
                'description': 'Título do filme'
                }
            }
        }
    }

    resposta = cliente.chat.completions.create(
        model='gpt-3.5-turbo', # 'gpt-4o' ou 'gpt-4o-mini' (nova versão)
        messages= historico,
        functions = [desc_funcao]
    )
    return resposta.choices[0].message

def pegar_nota(titulo):
    resultado = len(titulo) * random.random()
    nota = min(resultado%11, 10)
    return round(nota, 2)


resultado = enviar()

# executando a funcão
fn_call = resultado.function_call
params = json.loads(fn_call.arguments)
nome_funcao = eval(fn_call.name)
resultado_exec = nome_funcao(**params)

# enviar resultado para o modelo
historico.append({
    'role': 'function', 'name': fn_call.name, 'content': f'{resultado_exec}'
})

resultado = enviar()
print(resultado.content)


# texto_resposta = resposta.choices[0].message
# print(texto_resposta)