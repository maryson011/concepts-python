class SenhaForte:
    def __init__(self, valor):
        self.__valor = valor

        validacoes = [
            self.__tamanho_minimo(8),
            self.__tem_letras_maiusculas(),
            self.__tem_letras_minusculas(),
            self.__tem_numeros(),
            self.__tem_caracteres_especiais()
        ]

        if not all(validacoes):
            raise ValueError('Senha fraca')

    @property
    def valor(self):
        return self.__valor
    
    def __tamanho_minimo(self, qtde):
        return len(self.__valor) >= qtde
    
    def __tem_letras_maiusculas(self):
        return any(letra.isupper() for letra in self.__valor)
    
    def __tem_letras_minusculas(self):
        return any(letra.islower() for letra in self.__valor)
    
    def __tem_numeros(self):
        return any(letra.isdigit() for letra in self.__valor)
    
    def __tem_caracteres_especiais(self):
        return any(not letra.isalnum() for letra in self.__valor)



try:
    senha = SenhaForte('@1234Sew')
    print(senha.valor)
except ValueError as e:
    print(f'Ocorreu um erro {e}')
finally:
    print('FInalizou')