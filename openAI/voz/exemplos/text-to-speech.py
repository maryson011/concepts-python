from utils import cliente, arquivo

caminho_output = arquivo.formatar_caminho('fala.mp3', nome_pasta='audio')

resposta = cliente.audio.speech.create(
    model='tts-1', # ou tts-1-hd
    voice='onyx',
    input='Esse é um texto de teste com varias palavras legais e interessantes'
)

resposta.write_to_file(caminho_output)