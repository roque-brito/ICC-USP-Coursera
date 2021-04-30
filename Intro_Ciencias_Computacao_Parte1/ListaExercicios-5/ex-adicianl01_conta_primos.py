# Escreva a função n_primos que recebe como argumento um número inteiro maior ou igual a 
# 2 como parâmetro e devolve a quantidade de números primos que existem entre 2 e n (incluindo 2 e, se for o caso, n).
# --------------------------------------------------------------------------------------------------------------------

def n_primos(numero):
    #numero = int(input('Digite um número inteiro >= 2: '))
    while (numero < 2):
        print('Número inválido!')
        numero = int(input('Digite um número inteiro >= 2: '))
    c = 0
    n = 0
    while (n < numero):
        n += 1
        n1 = 0
        c1 = 0
        while n1 < n:
            n1 += 1
            
            resto = n % n1
            if resto != 0:
                p = ''
            else:
                c1 += 1
        if c1 == 2:
            c += 1
    return(c)

    
