# escrever função máximo que recebe 02 números inteiros como parâmetros e devolve o maior
# ----------------------------------------------------------------------
def maximo (x, y):
    if (x > y):
        maior = x
        print('Você digitou os números {} e {}'.format(x, y))
        print('O maior número digitado é o {}'.format(maior))
        
    else:
        maior = y
        print('Você digitou os números {} e {}'.format(x, y))
        print('O maior número digitado é o {}'.format(maior))
        
    return maior

x = int(input('Digite o primeiro número inteiro: '))
y = int(input('Digite o segundo número inteiro: '))

k = maximo(x, y)