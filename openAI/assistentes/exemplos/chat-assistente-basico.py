from utils import cliente
# 'asst_MgCHqkJzNvOmc037SLB5qjmM'
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
        run = self.cliente.beta.threads.runs.create_and_poll(
                thread_id = self.thread.id,
                assistant_id = self.id_assistente
            )

        if run.status == 'completed':
            mensagens = cliente.beta.threads.messages.list(
                thread_id = self.thread.id
            )
            return mensagens.data[0].content[0].text.value
            
    def iniciar(self):
        while True:
            mensagem = input('Você: ')
            if mensagem.lower() == 'sair':
                break
            self.mensagem_usuario(mensagem)
            resposta = self.computar_resposta()
            print(f'Assistente: {resposta}')

ChatAssistente(cliente, 'asst_MgCHqkJzNvOmc037SLB5qjmM').iniciar()