# criar listas por repetição:
# ---------------------------
print('-'*100)
a = [1, 2, 3]
b = [4, 5, 6]
b.append('bola')
a_triplicado = a * 3     # repete os elementos da lista "a" 3x, criando uma nova lista com esses elementos 
b_quintuplicado = b * 5  # repete os elementos da lista "b" 5x, criando uma nova lista com esses elementos

print(a_triplicado)
print(b_quintuplicado)
print('-'*100)
# ---------------------------------------------------------------------------------------------------------
del a[1] # exclui o elemento "1" da lista "a"
print(a)

lista = ['a','b', 'c', 'd', 'e', 'f']
print(lista)
del lista[1:5] 
print(lista)

