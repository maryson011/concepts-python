from utils import arquivo, OPENAI_API_KEY, requisicoes
import base64

caminho = arquivo.formatar_caminho('praia.png', nome_pasta='recursos')
imagem = ''

with open(caminho, 'rb') as img:
    imagem = base64.b64encode(img.read()).decode('utf-8')

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {OPENAI_API_KEY}'
}

payload = {
    'model':'gpt-4o',
    'messages':[
        {'role': 'system', 'content': 'Você é um descritor de imagens que descreve o conteúdo de imagens de maneira fidedigna e detalhada'},
        {'role': 'user', 'content': [
            {'type': 'text', 'text': 'O que tem nessa imagem? Me descreva brevemente'},
            {'type': 'image_url', 'image_url': {
                'url': f'data:image/png;base64,{imagem}'
            }}
        ]}
    ]
}

resposta = requisicoes.post("https://api.openai.com/v1/chat/completions", headers=headers, payload=payload)
print(resposta)