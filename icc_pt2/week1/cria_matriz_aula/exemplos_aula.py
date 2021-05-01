# Matrizes = lista de listas (no Python)
# Trata-se de uma estrutura de dados bidimensional com linhas e colunas (dahrr!)
# ===============================================================================
def cria_matriz(num_linhas, num_colunas, valor):
    ''' Cria matriz de elementos únicos. (int, int, valor)'''
    # Criar uma lista vazia:
    matriz = []
    for i in range(num_linhas):
        # criar uma linha "i":
        linha = []
        for j in range(num_colunas):
            linha.append(valor)
        # adiciona a linha a matriz:
        matriz.append(linha)
    
    return matriz

