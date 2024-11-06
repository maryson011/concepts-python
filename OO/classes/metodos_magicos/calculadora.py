class Calculadora:
    def __init__(self, valor_inicial=0):
        self.__valor = valor_inicial

    def somar(self, valor):
        self.__valor += valor
        return self

    def subtrair(self, valor):
        self.__valor -= valor
        return self
    
    def multiplicar(self, valor):
        self.__valor *= valor
        return self

    @property
    def valor(self):
        return self.__valor
    
    def __add__(self, outra_calc):
        return Calculadora(self.__valor + outra_calc.valor)
    
    def __str__(self) -> str:
        return f"A calculadora tem o valor em memoria de {self.__valor}"
    
    def __eq__(self, outra_calc):
        return self.__valor == outra_calc.valor
    
calc = Calculadora(100)
print(calc.valor)
calc.somar(20).subtrair(10).multiplicar(2) # Fluent API (return self)
print(calc.valor)

c2 = Calculadora(100).somar(2)

c3 = Calculadora(51).multiplicar(2)

c4 = c2 + c3
print(c4.valor)

print(c4)

print(c2 == c3)

# python magic methods