from utils import cliente, arquivo
import base64

resposta = cliente.images.generate(
    model="dall-e-3",
    prompt="um gato laranja brincando com um passarinho",
    size="1024x1024", # 1024x1024, 1024x1792, 1792x1024
    quality="standard", # standard ou hd
    style="vivid", # natural
    response_format='b64_json'
)

caminho_imagem = arquivo.formatar_caminho('imagem-base64.png')
with open(caminho_imagem, 'wb') as imagem:
    conteudo = resposta.data[0].b64_json
    imagem.write(base64.urlsafe_b64decode(conteudo))
