# Escreva a função maior_primo que recebe um número inteiro maior ou igual a 2 como parâmetro e 
# devolve o maior número primo menor ou igual ao número passado à função;
# ----------------------------------------------------------------------------------------------
def éPrimo (k):
    for i in range (1, k+1, 1):
        cont = 0
        for j in range (1, k+1, 1):
            resto = (i % j)
            if resto != 0:
                p = '' 
            else:
                cont += 1
        if cont == 2:
            primo = i 
    print('O número {} é o maior primo'.format(primo))
    return (primo)

def maior_primo (n):
    return éPrimo(k)

k = int(input('Digite um númeo iteiro: '))
MaiorPrimo = maior_primo(k)
