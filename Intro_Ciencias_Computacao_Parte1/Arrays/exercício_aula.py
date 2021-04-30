# ----------------------------------------------------------------------------------------------------------------------
# Ler do teclado uma sequencia de numeros inteiros terminadas por zero. Quando o usuário digita zero, o programa imprime
# a sequencia na ordem inversa - ao contrário da ordem que o usuário digitou;
# ----------------------------------------------------------------------------------------------------------------------
lista1 = []
n = 1
while n != 0:
    n = int(input('Digite um número: '))
    lista1.append(n)

print(lista1)
l = len(lista1)
print('Número de ítens na lista criada = ', l)

i = l
while i > 0:
    i = i-1
    k = lista1[i]
    print(k)
 
