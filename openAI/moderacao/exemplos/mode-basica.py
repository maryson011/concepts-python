from utils import cliente

mensagem = 'Vou na sua casa te abraçar'

resposta = cliente.moderations.create(input=mensagem)
resultado = resposta.results[0]
print(resultado.categories.to_json())
print('Impróprio? ', resultado.flagged)