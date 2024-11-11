from utils import cliente, arquivo

caminho_output = arquivo.formatar_caminho('params.mp3', nome_pasta='audio')

resposta = cliente.audio.speech.create(
    model='tts-1', # ou tts-1-hd
    voice='onyx',
    input='Esse é um texto de teste, e tem como objetivo testar os modelos de audio da openai.',
    speed=0.75,
    response_format='mp3' # mp3, opuc, aac, flac, wav e pcm
)

resposta.write_to_file(caminho_output)