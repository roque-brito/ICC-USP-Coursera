def cria_matriz(num_linhas, num_colunas):
    '''
    (int, int) -> matriz(lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é digitado pelo usuário.
    '''
    # Criar uma lista vazia:
    matriz = []
    for i in range(num_linhas):
        # criar uma linha "i":
        linha = []
        for j in range(num_colunas):
            elemento = float(input('Digite o elemento ['+str(i)+']['+str(j)+']: '))
            linha.append(elemento)
        # adiciona a linha a matriz:
        matriz.append(linha)
    
    return matriz

def main():
    '''Métodos para entrada de valores para o número de linhas e colunas da matriz.'''

    i = int(input('Informe o número de linhas da matriz: '))
    j = int(input('Informa o número de colunas da matriz: '))
    matriz = cria_matriz(i, j)
    
    return(matriz)

m = main()

def ordena_matriz(matriz):
    ''' Método para ordenar a matriz para melhorar a leitura: Cada linha da matriz em uma nova linha. '''
    k = len(matriz)
    for i in range(len(matriz)):
        print(matriz[i])

    return ()

ordena_matriz(m)
