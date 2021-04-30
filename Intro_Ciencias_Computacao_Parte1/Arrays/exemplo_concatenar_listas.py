# concatenar listas = juntar listas
# ----------------------------------------------------------
a = [1, 2]
b = [3, 4]
c = [5, 6]

# O método "append" altera uma lista adicionando um elemento ao final da lista
b.append('gato')

# concatenar cria uma nova lista!
lista = a + b + c + [7]
print(lista)