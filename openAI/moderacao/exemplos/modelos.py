from utils import cliente, arquivo

mensagem = 'Vou na sua casa te bater'

resposta_stable = cliente.moderations.create(
        input=mensagem,
        model='text-moderation-stable'
    )

caminho_stable = arquivo.formatar_caminho('stable.json')
with open(caminho_stable, 'w') as arq:
    arq.write(resposta_stable.to_json())

resposta_latest = cliente.moderations.create(
        input=mensagem,
        model='text-moderation-latest'
    )

caminho_latest = arquivo.formatar_caminho('latest.json')
with open(caminho_latest, 'w') as arq:
    arq.write(resposta_latest.to_json())