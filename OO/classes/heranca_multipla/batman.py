class Carro:
    def dirigir(self):
        return "VOcÊ está derigindo"
    

class Barco:
    def navegar(self):
        return "Você está navegando"
    
class Aviao:
    def voar(self):
        return "VOcê está voando"
    
class CarroAnfibio(Carro, Barco):
    pass

c1 = CarroAnfibio()
print(c1.dirigir())
print(c1.navegar())

class Batmovel(Carro, Barco, Aviao):
    pass

c2 = Batmovel()
print(c2.dirigir())
print(c2.navegar())
print(c2.voar())