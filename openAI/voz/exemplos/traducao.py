from utils import cliente, arquivo

caminho_input = arquivo.formatar_caminho('fala.mp3', nome_pasta='audio')

arquivo_audio = open(caminho_input, 'rb')

traducao = cliente.audio.translations.create(
    model='whisper-1',
    file= arquivo_audio,
    response_format='text'
)

print(traducao)