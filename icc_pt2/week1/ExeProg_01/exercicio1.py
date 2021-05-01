''' Escreva uma função dimensoes(matriz) que recebe uma matriz como parâmetro e imprime as dimensões da matriz recebida, no formato iXj. '''
def dimensoes(matriz):
    m = len(matriz)  # número de linhas
    for i in range(len(matriz)):
        linha = matriz[i]
        n = len(linha)
    print(''+str(m)+'X'+str(n))
    
    return
