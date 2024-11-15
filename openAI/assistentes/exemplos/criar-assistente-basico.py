from utils import cliente

assistente = cliente.beta.assistants.create(
    name = 'tapioca',
    instructions = 'Você é um assistente útil, apaixonado por tapioca.',
    model = 'gpt-3.5-turbo',
    description = 'Assistente obsecado por tapioca',
    temperature = 1,
    response_format = 'auto' # valor padrão, ou json_object
)

print(assistente)