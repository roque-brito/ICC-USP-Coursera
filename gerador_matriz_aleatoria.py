from random import randint
def crie_matriz(i_linhas, j_colunas, n):
    ''' (int, int, valor) -> matriz(lista de listas)
    Cria e retorna uma matriz com "i" linhas e "j" colunas
    em que cada elemento é igual ao valor dado.
    '''
    # Cria matriz mazia:
    matriz = []
    for i in range(i_linhas):
        # Cria a linha "i" - a linha já contém as colunas:
        # Cria uma lista (linha) vazia:
        linha = [] 
        for j in range(j_colunas):
            linha += [randint(-15,50)]
        # Inserir a linha criada na matriz -> "matriz recebe linha":
        matriz += [linha]
    return(matriz)
A = crie_matriz( 5, 5, 0)
print('Matriz de "zeros" = lista de listas => ', A)

def imprime_matriz(A):
    n_linhas = len(A)
    n_colunas = len(A[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            minimmo = min(A[i])
            maximo = max(A[i])
        linha = A[i]
        print(f'{linha}')
        
    return(A)
imprime_matriz(A)
