# clonando listas
# --------------------------------------------------------------------------------------------------------
print('-'*100)
lista1 = ['vermelho', 'verde', 'azul']
print(lista1)
print('-'*100)
# --------------------------------------------------------------------------------------------------------
# CRIANDO UM CLONE DE UMA LISTA:
# --------------------------------------------------------------------------------------------------------
lista2 = []
def clone(lista):
    clone = []
    for objeto in lista:
        clone.append(objeto)
    return clone
lista2 = clone(lista1)
lista2[0] = 'rosa'

print(lista1)
print(lista2)

# --------------------------------------------------------------------------------------------------------
# CRIANDO UM CLONE DE UMA LISTA DE UM JEITO MAIS FÁCIL:
# --------------------------------------------------------------------------------------------------------
lista2 = lista1[:]
lista2[0] = 'rosa'
print(lista1)
print(lista2)
# --------------------------------------------------------------------------------------------------------
# VERIFICANDO BOOLEANO EM LISTAS...
# --------------------------------------------------------------------------------------------------------
print('rosa' in lista1)
print('rosa' in lista2)

if 'rosa' in lista1:
    print('Está')
else:
    print('Não está')
if 'rosa' in lista2:
    print('Está')
else:
    print('Não está')