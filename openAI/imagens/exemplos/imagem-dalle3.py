from utils import cliente, arquivo

resposta = cliente.images.generate(
    model="dall-e-3",
    prompt="um gato laranja brincando com um passarinho",
    size="1024x1024", # 1024x1024, 1024x1792, 1792x1024
    quality="standard", # standard ou hd
    style="vivid" # natural
)

url = resposta.data[0].url

arquivo.salvar_imagem(url, 'dalle3.png')