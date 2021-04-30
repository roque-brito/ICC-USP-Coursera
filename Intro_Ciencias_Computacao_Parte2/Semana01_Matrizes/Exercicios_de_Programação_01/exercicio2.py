''' Escreva a função soma_matrizes(m1, m2) que recebe 2 matrizes e devolve uma matriz
que represente sua soma caso as matrizes tenham dimensões iguais. Caso contrário,
a função deve devolver False. '''
# ======================================================================================

def dimensoes(matriz):
    m = len(matriz)  # número de linhas
    for i in range(len(matriz)):
        linha = matriz[i]
        n = len(linha)
    return (m, n)

def teste_dimensoes(m1, m2):
    teste_m1 = dimensoes(m1)
    teste_m2 = dimensoes(m2)

    if teste_m1 != teste_m2:
        return False
    else:
        return True

def soma_matrizes(m1, m2):
    teste = teste_dimensoes(m1, m2)
    if teste == True:
        matriz_soma = []
        for i in range(len(m1)):
            linha_m3 = []
            for j in range(len(m1[i])):
                termo_m1 = m1[i][j]
                termo_m2 = m2[i][j]
                termo_m3 = termo_m1 + termo_m2
                linha_m3.append(termo_m3)
            matriz_soma.append(linha_m3)
    else:
        return False
    
    return matriz_soma
'''
m1 = [[1], [2], [3]]
m2 = [[2, 3, 4], [5, 6, 7]]

#m1 = [[1, 2, 3], [4, 5, 6]]
#m2 = [[2, 3, 4], [5, 6, 7]]'''
