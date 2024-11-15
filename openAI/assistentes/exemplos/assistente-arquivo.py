from utils import cliente, arquivo

caminho_produtos = arquivo.formatar_caminho('produtos.pdf', nome_pasta = 'recursos')

def criar_assistente_com_arquivo():
    store = cliente.beta.vector_stores.create(name='Produtos')
    batch = cliente.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id = store.id,
        files = [open(caminho_produtos, 'rb')]
    )

    print(f'id store = {store.id}, status batch = {batch.status}')

    assistente = cliente.beta.assistants.create(
        name = 'Consultor',
        instructions = 'Você é um especialista em equipamentos tecnologicos e tem um vasto conhecimento de aspectos técnicos com processadores, memória RAM e outros quesitos importantes para opinar sobre a qualidade de produtos. Seu principal objetico é ajudar clientes a encontrarem o melhor produto para atender suas necessidades.',
        model = 'gpt-3.5-turbo',
        tools = [{'type': 'file_search'}],
        tool_resources = {'file_search': {'vector_store_ids': [store.id]}}
    )

    print(f'Id Assistente = {assistente.id}')

criar_assistente_com_arquivo()