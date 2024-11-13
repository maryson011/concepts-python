from utils import cliente

resposta = cliente.chat.completions.create(
    model='gpt-4o',
    messages=[
        {'role': 'system', 'content': 'Você é um descritor de imagens que descreve o conteúdo de imagens de maneira fidedigna e detalhada'},
        {'role': 'user', 'content': [
            {'type': 'text', 'text': 'O que tem nessa imagem? Me descreva brevemente'},
            {'type': 'image_url', 'image_url': {
                'url': 'https://decoragpt.com.br/storage/2023/12/decoracao-cozinha-loft.jpg'
            }}
        ]}
    ]
)

print(resposta.choices[0].message.content)