from utils import cliente, arquivo

def criar_arquivos():
    caminho_treinamento = arquivo.formatar_caminho('dados-treinamento.jsonl', nome_pasta='recursos')
    caminho_validacao = arquivo.formatar_caminho('dados-validacao.jsonl', nome_pasta='recursos')

    arquivo_treinamento = cliente.files.create(
        file = open(caminho_treinamento, 'rb'),
        purpose = 'fine-tune'
    )

    print(f'Id treinamento: {arquivo_treinamento.id}')

    arquivo_validacao = cliente.files.create(
        file = open(caminho_validacao, 'rb'),
        purpose = 'fine-tune'
    )

    print(f'Id validacao: {arquivo_validacao.id}')

id_validacao = 'file-ZpIZE067A8XVzOL3hVbBBbSl'
id_treinamento = 'file-UxNA4sbOCNCTyFjASsGwdoTY'

job = cliente.fine_tuning.jobs.create(
    training_file=id_treinamento,
    validation_file=id_validacao,
    model='gpt-3.5-turbo',
    suffix='emojus2'
)

print(job.id)