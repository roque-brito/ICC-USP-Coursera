def imprime_matriz(m):
    '''Método para ordenar a matriz para melhorar a leitura: Cada linha da matriz em uma nova linha.'''
    n = []
    for i in range(len(m)):
        linha  = m[i]
        print(' '.join(str(elemento) for elemento in linha))    
    return
#m = [[1, 2], [3, 4]]
m = [[1, 2, 7], [3, 4, 8], [1, 2, 3]]
imprime_matriz(m)
