def executar_divisao(tentativas = 1):
    try:
        divisor = int(input('Informe o divisor: '))
        return 1000 / divisor
    except Exception as e:
        if tentativas > 5:
            raise e
        print(f'Ocorreu um erro... {e}')
        print(f'Tentativa {tentativas}/5')
        return executar_divisao(tentativas + 1)
    
resultado = executar_divisao()
print(f'O resultado é: {resultado}')