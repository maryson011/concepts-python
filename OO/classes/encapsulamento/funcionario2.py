class Funcinario:
    def __init__(self, salario):
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario
    
    def movimentacao_salarial(self, percentual):
        if percentual < 0:
            raise ValueError('Percentual invalido!!')
        self.__salario = self.__salario + ((self.__salario * percentual) / 100)

func = Funcinario(2000)
func.movimentacao_salarial(50)
print(func.salario)