from utils import cliente, arquivo

resposta = cliente.images.generate(
    model="dall-e-2",
    prompt="um gato laranja brincando com um passarinho",
    size="1024x1024", # 256x256, 512x512, 1024x1024
    n=2 # entre 1 e 10 imagens
)
for i, imagem in enumerate(resposta.data):
    arquivo.salvar_imagem(imagem.url, f'dalle2_{i}.png')
    print(f'imagem {i} foi salva')

