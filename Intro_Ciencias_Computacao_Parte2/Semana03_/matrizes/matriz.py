# módulo para criar matrizes:
# ============================
def cria_matriz(num_linhas, num_colunas, elemento):
    ''' (int, int, valor) -> matriz(lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas colunas
    em cada elemento é igual ao valor do elemento inserido pelo usuário'''

    matriz = []
    for i in range(num_linhas):
        # cria a linha i
        linha = [] # lista vazia
        for j in range(num_colunas):
            linha.append(elemento)
    
        # adiciona a linha à matriz
        matriz.append(linha)
    
    return matriz
