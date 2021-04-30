# código ERRADO
def cria_matriz1(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_colunas):
        coluna = []
        for j in range(num_linhas):
            valor = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))
            coluna.append(valor)
        matriz.append(coluna)
    return matriz
# ----------------------------------------------------------------------------
# código ERRADO E COM ERRO

def cria_matriz2(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        coluna = []
        for j in range(num_colunas):
            coluna.append(0)
        matriz.append(coluna)

    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[j][i] = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))

    return matriz
# ----------------------------------------------------------------------------
# código ERRADO E COM ERRO
def cria_matriz3(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        coluna = []
        for j in range(num_colunas):
            coluna.append(0)
        matriz.append(coluna)

    for i in range(num_linhas):
        for j in range(num_colunas):
            matriz[j][i] = int(input("Digite o elemento [" + str(i) + "][" + str(j) + "]: "))

    return matriz
# ----------------------------------------------------------------------------
''' código CORRETO!
Este código faz com que primeiramente toda a primeira linha seja preenchida, em seguida a segunda e assim sucessivamente. Se nós quiséssemos que a primeira coluna fosse preenchida e em seguida a segunda coluna e assim por diante, como ficaria o código?

Um exemplo: se o usuário digitasse o seguinte comando “x = cria_matriz(2,3)” e em seguida informasse os seis números para serem armazenados na matriz, na seguinte ordem: 1, 2, 3, 4, 5, 6; o x teria ao final da função a seguinte matriz: [[1, 3, 5], [2, 4, 6]].

'''
def cria_matriz4(num_linhas, num_colunas):
    matriz = []  #lista vazia
    for i in range(num_linhas):
        linha = []
        for j in range(num_colunas):
            linha.append(0)
        matriz.append(linha)

    for i in range(num_colunas):
        for j in range(num_linhas):
            matriz[j][i] = int(input("Digite o elemento [" + str(j) + "][" + str(i) + "]: "))

    return matriz
