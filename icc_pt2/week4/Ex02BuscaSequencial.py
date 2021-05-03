
def busca(lista, elemento):
    ''' (list, float) --> bool '''
    cont = 0
    for i in range(len(lista)):
        
        if lista[i] == elemento:
            return i
        else:
            cont += 1
        
    if cont == len(lista):
        return False
        
if __name__ == '__main__':

    lista1 = ['a', 'e', 'i', 'o', 'u']

    lista2 = [12, 13, 14]

    x = busca(lista1, 'e')
    y = busca(lista2, 15)
    
    print(x)
    print(y)