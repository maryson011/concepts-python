class Funcinario:
    def __init__(self, salario):
        self.nome = 'teste'
        self.__salario = salario

    # GETTER
    def get_salario(self):
        return self.__salario
    
    # PROPRIEDADE
    @property
    def salario(self):
        return self.__salario
    
    @salario.setter
    def salario(self, novo_salario):
        if novo_salario <= self.__salario:
            raise ValueError("O valor não pode ser menor que o salário atual!!!")
        self.__salario = novo_salario

    def set_salario(self, novo_salario):
        self.__salario = novo_salario

func = Funcinario(1000)
print(func.get_salario())
print(func.nome)
print(func.salario)
func.salario = 1900
print(func.salario)
func.set_salario(2200)
print(func.salario)