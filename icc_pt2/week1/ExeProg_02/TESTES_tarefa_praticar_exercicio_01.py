def imprime_matriz(m):
    '''Método para ordenar a matriz para melhorar a leitura: Cada linha da matriz em uma nova linha.'''
    for i in range(len(m)):
        linha  = m[i]
        for j in range(len(linha)):
            print(f'{m[i][j]:^2}', end='')
        print()
                
    return


def test_print_matriz():
    m1 = [[1], [2]]
    m2 = [[1, 2], [3, 4]]
    m3 = [[1, 2, 3], [4, 5, 6]]
    m4 = [[1, 2, 7], [3, 4, 8], [1, 2, 3]]
    m5 = [[1, 2], [3, 4]]
    matriz = imprime_matriz(m4)
    
    return

test_print_matriz()
