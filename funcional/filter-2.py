class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def __str__(self) -> str:
        return f'Cliente {self.nome} tem {self.email}'

lista_clientes = [
    Cliente('João', 'j@email'),
    Cliente('Maria', 'm@email'),
    Cliente('Rita', 'r@empresa'),
    Cliente('Pedro', 'p@email'),
    Cliente('Paulo', 'p@empresa'),
]

r1 = filter(lambda c: "@empresa" in c.email, lista_clientes)
clientes_filtrados = list(r1)

for cliente in clientes_filtrados:
    print(cliente)