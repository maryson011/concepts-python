from abc import ABC, abstractmethod

class Atendente(ABC):
    @abstractmethod
    def saudacao(self):
        pass

class AtendentePt(Atendente):
    def saudacao(self):
        return "Bom dia"
    
class AtendenteEn(Atendente):
    def saudacao(self):
        return "Good Morning"

a1 = AtendentePt()

print(a1.saudacao())

a1 = AtendenteEn()
print(a1.saudacao())

# @abstractmethod
# um metodo abstrato precisa ser implementado nas classes filhas a não sser que as
# classes filhas também sejam abstratas.