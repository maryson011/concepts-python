from typing import override
from utils import cliente, AssistantEventHandler

class EventHandler(AssistantEventHandler):
    
    @override
    def on_text_created(self, text):
        print(f'Assistente: ', end='', flush=True)

    @override
    def on_text_delta(self, delta, snapshop):
        print(delta.value, end='', flush=True)

    def on_text_done(self, snapshop):
        print()

class ChatAssistente:
    def __init__(self, cliente, id_assistente):
        self.cliente = cliente
        self.id_assistente = id_assistente
        self.thread = self.cliente.beta.threads.create()

    def mensagem_usuario(self, mensagem):
        return self.cliente.beta.threads.messages.create(
                thread_id = self.thread.id,
                role = 'user',
                content = mensagem
            )
    
    def computar_resposta(self):
        with self.cliente.beta.threads.runs.stream(
            thread_id = self.thread.id,
            assistant_id = self.id_assistente,
            event_handler = EventHandler()
        ) as stream:
            stream.until_done()
            
    def iniciar(self):
        while True:
            mensagem = input('Você: ')
            if mensagem.lower() == 'sair':
                break
            self.mensagem_usuario(mensagem)
            self.computar_resposta()
            

ChatAssistente(cliente, 'asst_MgCHqkJzNvOmc037SLB5qjmM').iniciar()