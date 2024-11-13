from utils import cliente, arquivo

caminho_imagem = arquivo.formatar_caminho('praia.png', nome_pasta='recursos')

resposta = cliente.images.create_variation(
    model="dall-e-2", # verificar se há disponibilidade de outro modelo
    image= open(caminho_imagem, 'rb'),
    size="1024x1024", # 256x256, 512x512, 1024x1024
    n=3
)
for i, imagem in enumerate(resposta.data):
    arquivo.salvar_imagem(imagem.url, f'variante_{i}.png')
    print(f'imagem {i} foi salva')

