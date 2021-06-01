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