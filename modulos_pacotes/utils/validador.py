class Validador:
    def __init__(self, valor, atributo, erros=[]):
        self.__valor = valor
        self.__atributo = atributo
        self.__erros = erros

    @property
    def valor(self):
        if self.__erros:
            raise ValueError(self.__erros)
        return self.__valor
    
    def nao_nulo(self):
        if self.__valor == None:
            self.__erros.append(f'{self.__atributo}: não pode ser nulo!')
        return self
    
    def nao_vazio(self):
        if self.__valor == None:
            return self
        
        if not self.__valor.strip():
            self.__erros.append(f'{self.__atributo}: não pode ser vazio!')
        return self
    
    def tamanho_minimo(self, minimo):
        if self.__valor == None:
            return self
        
        if len(self.__valor) < minimo:
            self.__erros.append(f'{self.__atributo}: deve possuir o tamanho minimo de {minimo}!')
        return self
    
    def tamanho_maximo(self, maximo):
        if self.__valor == None:
            return self
        
        if len(self.__valor) > maximo:
            self.__erros.append(f'{self.__atributo}: deve possuir o tamanho maximo de {maximo}!')
        return self
    
    def qtde_min_palavras(self, qtde):
        if self.__valor == None:
            return self
        
        if len(self.__valor.split()) < qtde:
            self.__erros.append(
                f'{self.__atributo}: deve possuir pelo menos {qtde}!')
        return self
    
    def email(self):
        if self.__valor == None:
            return self
        
        if '@' not in self.__valor:
            self.__erros.append(f'{self.__atributo}: deve ser um e-mail válido!')
        return self