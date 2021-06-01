# Implemente a função insertion_sort(lista), que recebe uma lista com números inteiros como parâmetro e devolve esta lista ordenada. 
# Utilize o algoritmo insertion sort.
# ==================================================================================================================================
from random import randrange

# Gerador de lista aleatória:
def lista_aleatoria(n):
    lista = [randrange(100) for x in range(n)]
    return lista

# [1, 6, 88, 80, 63, 5, 72, 0, 73, 71]
def testa_crescente(lista):
    ''' [list] --> bool 
        Retorna True se a lista estiver em ordem crescente
        e False caso contrpario '''
    cont = 0
    tam = len(lista)
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False         
        else:
            cont += 1
        if cont == len(lista) - 1:
            return True

def insertion_sort(lista):
    ''' [list] --> [list] 
        Retorna uma lista ordenada do menor para o maior '''
    for i in range(len(lista)):
        elemento = lista[i]       
        j = i
        while j > 0 and lista[j-1] > elemento:
            lista[j] = lista[j-1]
            j = j - 1
        lista[j] = elemento
    
    return lista
    
# ------------ Teste ------------
if __name__ == '__main__':
    n = 10
    #lista = [1, 6, 88, 80, 63, 5, 72, 0, 73, 71]
    lista = lista_aleatoria(n)
    print(f'Lista desordenada: {lista}')

    teste = testa_crescente(lista)
    print(teste)

    lista_ordenada = insertion_sort(lista)
    print(f'Lista ordenada: {lista_ordenada}')
    
    teste = testa_crescente(lista_ordenada)
    print(teste)