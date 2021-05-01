def sao_multiplicaveis(m1, m2):
    n_colunas = len(m1[0])
    n_linhas = len(m2)
    if n_colunas == n_linhas:
        return True
    else:
        return False
    
def teste():
    m1 = [[1, 2, 3], [4, 5, 6]]
    m2 = [[2, 3, 4], [5, 6, 7]]
    m3 = [[1], [2], [3]]
    m4 = [[1, 2, 3]]
    y = sao_multiplicaveis(m3, m4)
    return y
x = teste()
print(x)
