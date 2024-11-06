## marca, nome

class Carro():
    def __init__(self, nome, marca, velocidade=0):
        self.nome = nome
        self.marca = marca
        self.veloidade = velocidade

    def buzinar(self, qtde=1):
        for i in range(qtde):
            print(f"{self.marca} {self.nome} => Biiiii")

    def acelerar(self):
        self.veloidade += 10

    def frear(self):
        self.veloidade -= 10

c1 = Carro('Palio', 'Fiate')
c2 = Carro('Civic', 'Honda')

c1.buzinar()
c1.acelerar()
c1.acelerar()

print(c1.nome, c1.marca)
print(c1.veloidade)
c1.frear()
print(c1.veloidade)
print(c2.nome, c2.marca)