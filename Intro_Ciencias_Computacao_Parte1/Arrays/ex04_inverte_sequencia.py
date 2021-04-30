# ----------------------------------------------------------------------------------------------------------------------
# Ler do teclado uma sequencia de numeros inteiros terminadas por zero. Quando o usuário digita zero, o programa imprime
# a sequencia na ordem inversa - ao contrário da ordem que o usuário digitou;
# note: o "0" não deve fazer parte da sequência!
# ----------------------------------------------------------------------------------------------------------------------
lista = []
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    lista.append(n)

del(lista[-1])
#lista1.reverse()

i = len(lista)
while i > 0:
    i -= 1
    k = lista[i]
    print(k)

print(type(lista))