def cria_matriz(num_linhas, num_colunas):
    matriz = []
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            valor = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]"))
            linha.append(valor)
        matriz.append(linha)
    return matriz


def le_matriz():
    lin = int(input("Digite o numero de linhas da matriz:"))
    col = int(input("Digite o numero de colunas da matriz: "))
    return cria_matriz(lin, col)


m = le_matriz()

for row in m:
    for val in row:
        print(f'{val:2}')
    print
