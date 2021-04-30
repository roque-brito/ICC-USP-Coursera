#------------------------------------------------------------------------
# Escreva uma função 'soma_hipotenusas' que receba como parâmetro um
# número inteiro positivo e retorna a soma de todos os inteiros
# entre 1 e n que são comprimento da hipotenusa de algum triângulo
# retângulo com catetos inteiros.
#------------------------------------------------------------------------
def calcula_hipotenusa(i, j):
    h = ((i*i) + (j*j))
    return(h)

def é_hipotenusa(n):
    n1 = 0
    soma = 0
    while n1 < n:
        n1 += 1
        N = n1*n1
        i = 0
        j = 1
        while i < n1:
            i += 1
            while j < n1:
                j += 1
                H = calcula_hipotenusa(i, j)
                if H == N:
                    soma += n1
                    i = n
            j = i
    return(soma)

def soma_hipotenusas(n):
    soma_H = é_hipotenusa(n)
    return(soma_H)

