def sao_multiplicaveis(m1, m2):
    n_colunas = len(m1[0])
    n_linhas = len(m2)
    if n_colunas == n_linhas:
        return True
    else:
        return False