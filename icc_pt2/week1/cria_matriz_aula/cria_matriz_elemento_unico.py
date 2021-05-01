def cria_matriz(num_linhas, num_colunas, valor):
    '''
    (int, int, valor) -> matriz(lista de listas)
    Cria e retorna uma matriz com num_linhas linhas e num_colunas
    colunas em que cada elemento é igual  ao valor dado (valores iguais)
    '''

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

def main():
    i = int(input('Informe o número de linhas da matriz: '))
    j = int(input('Informa o número de colunas da matriz: '))
    n = float(input('Informe o valor dos elementos na matriz: '))
    matriz = cria_matriz(i, j, n)
    print(matriz)
    return(matriz)
main()