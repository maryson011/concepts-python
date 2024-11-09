class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

lista_clientes = [
    Cliente('João', 'j@email'),
    Cliente('Maria', 'm@email'),
    Cliente('Pedro', 'p@email')
]

lista_emails = list(map(lambda c: c.email, lista_clientes))
print(lista_emails)
