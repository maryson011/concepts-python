from utils import cliente, arquivo

caminho_imagem = arquivo.formatar_caminho('praia.png', nome_pasta='recursos')
caminho_mascara = arquivo.formatar_caminho('praia-mask.png', nome_pasta='recursos')

resposta = cliente.images.edit(
    model="dall-e-2", # verificar se há disponibilidade de outro modelo
    image= open(caminho_imagem, 'rb'),
    mask= open(caminho_mascara, 'rb'),
    prompt="A visão da praia em um dia ensolarado com o mar calmo e aviões coloridos voando no céu",
    size="1024x1024", # 256x256, 512x512, 1024x1024
)
for i, imagem in enumerate(resposta.data):
    arquivo.salvar_imagem(imagem.url, f'edicao_{i}.png')
    print(f'imagem {i} foi salva')

