import time
from utils import cliente, arquivo
import sounddevice as sd # type: ignore
import soundfile as sf # type: ignore
from pydub import AudioSegment # type: ignore
from pydub.playback import play # type: ignore
import re

class Chat:
    def __init__(self):
        self.usuario_temp_file = arquivo.formatar_caminho('usuario_temp.mp3', nome_pasta='audio')
        self.assistente_temp_file = arquivo.formatar_caminho('assistente_temp.mp3', nome_pasta='audio')
        self.cliente = cliente
        self.historico = [
            {
                'role': 'system',
                'content': 'Você é uma assistente útil'
            }
        ]

    def aviso(self, texto):
        print('\033[34m' + texto + '\033[0m')
    
    def gravar(self, duracao = 5):
        sample_rate = 44100
        total_samples = int(sample_rate * duracao)

        gravacao = sd.rec(total_samples, samplerate=sample_rate, channels=1)

        self.aviso('Seu audio acaba em...')
        for i in range (duracao, 0, -1):
            self.aviso(f'{i}...')
            time.sleep(1)

        sd.wait()

        sf.write(self.usuario_temp_file, gravacao, sample_rate)

    def transcrever(self):
        arquivo_audio = open(self.usuario_temp_file, 'rb')
        transcricao = self.cliente.audio.transcriptions.create(
            model='whisper-1',
            file= arquivo_audio,
            response_format='text'
        )
        return transcricao
    
    def buscar_resposta(self, texto):
        self.historico.append(
            {
                'role': 'user',
                'content': texto
            }
        )

        resposta = self.cliente.chat.completions.create(
            model='gpt-3.5-turbo',
            messages=self.historico
        )

        texto_resposta = resposta.choices[0].message.content

        self.historico.append(
            {
                'role': 'assistant',
                'content': texto_resposta
            }
        )

        return texto_resposta
    
    def falar_resposta(self, texto):
        resposta = self.cliente.audio.speech.create(
            model='tts-1',
            voice='onyx',
            input=texto,
            speed=0.75
        )

        resposta.write_to_file(self.assistente_temp_file)
        audio = AudioSegment.from_mp3(self.assistente_temp_file)
        play(audio)
    
    def iniciar(self):
        self.aviso('Iniciando...')
        while True:
            self.aviso('Prepare-se para falar. Aperte enter quando estiver pronto')
            input()
            self.gravar()
            self.aviso('Está feliz com sua mensagem? S/n')
            esta_feliz = input()
            if esta_feliz.lower() == 'n':
                continue
            self.aviso('Audio em processamento...')
            texto = self.transcrever()
            if re.search(r"ok.?", texto, re.IGNORECASE):
                break
            self.aviso('Processando resposta...')
            resposta = self.buscar_resposta(texto)
            self.falar_resposta(resposta)

Chat().iniciar()