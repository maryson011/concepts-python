class Pessoa:
    def __init__(self, nome, idade, sexo):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo

p1 = Pessoa('Bia', 32, 'Female')
print(p1.nome, p1.idade, p1.sexo)

p2 = Pessoa('RIta', 33, 'Female')
print(p2.nome)