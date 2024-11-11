from utils import cliente, arquivo

caminho_input = arquivo.formatar_caminho('fala.mp3', nome_pasta='audio')

arquivo_audio = open(caminho_input, 'rb')

transcricao = cliente.audio.transcriptions.create(
    model='whisper-1',
    file= arquivo_audio,
    response_format='text',
    language='pt'
)

print(transcricao)