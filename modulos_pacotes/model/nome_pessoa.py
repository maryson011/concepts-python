from utils.validador import Validador

class NomePessoa:
    def __init__(self, completo, atributo='Nome'):
        self.__completo = Validador(
            completo, atributo).nao_nulo().nao_vazio().tamanho_minimo(4).tamanho_maximo(120).qtde_min_palavras(2).valor

    @property
    def completo(self):
        return self.__completo

    @property
    def primeiro_nome(self):
        return self.__completo.split()[0]

    @property
    def ultimo_sobrenome(self):
        return self.__completo.split()[-1]
    
    @property
    def segundo_nome(self):
        partes_nome = self.__completo.split()
        if len(partes_nome) > 1:
            return partes_nome[1]
        else:
            return partes_nome[0]
    
    def __str__(self) -> str:
        return self.__completo