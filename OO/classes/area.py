class Areas:
    PI = 3.14

    #@staticmethod
    @classmethod
    def circulo(cls, raio):
        return cls.PI * raio ** 2
    
    @staticmethod
    def triangulo(base, altura):
        return (base * altura) / 2
    
    @classmethod
    def alterar_pi(cls, novo):
        cls.PI = novo

    def retangulo(base, altura):
        return base * altura

print(Areas.PI)
Areas.alterar_pi(3.1415)
print(Areas.circulo(2.5))
print(Areas.triangulo(6,10))
print(Areas.retangulo(10, 100))
