from utils import cliente

id_assistente = 'asst_MgCHqkJzNvOmc037SLB5qjmM'

thread = cliente.beta.threads.create(

)

mensagem_usuario = cliente.beta.threads.messages.create(
    thread_id = thread.id,
    role = 'user',
    content = 'Bom dia.'
)

run = cliente.beta.threads.runs.create_and_poll(
    thread_id = thread.id,
    assistant_id = id_assistente
)

if run.status == 'completed':
    mensagens = cliente.beta.threads.messages.list(
        thread_id = thread.id
    )
    historico = [
        {
            'quem':mensagem.role, 
            'texto': mensagem.content[0].text.value
        } for mensagem in mensagens
    ]
    historico.reverse()
    print(historico)