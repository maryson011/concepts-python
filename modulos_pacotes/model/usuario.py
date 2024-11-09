from .email import Email
from .nome_pessoa import NomePessoa

class Usuario:
    def __init__(self, nome, email):
        self.nome = NomePessoa(nome, 'Nome usuário')
        self.email = Email(email)

    def __str__(self) -> str:
        return f'usuario: {self.nome} {self.email.valor}'