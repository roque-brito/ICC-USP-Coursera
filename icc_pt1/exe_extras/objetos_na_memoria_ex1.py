# lista de temperaturas 
# Qual o dia das temperaturas mais baixa e mais alta:

def MinMax(temperaturas):
    print('A menor temperatra do mê foi: ', minima(temperaturas), '°C')
    print('A maior temperatra do mê foi: ', maxima(temperaturas), '°C')

def minima(temps):
    min = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i += 1
    return min

def maxima(temps):
    max = temps[0]
    i = 0
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i += 1
    return max

def teste_pontual(temp, valor_esperado):
    valor_calculado = minima(temp)
    if minima(temp) != valor_esperado:
        print('Valor errado para array', temp)
        print('Valor esperado: ', valor_esperado, 'Valor calculado: ', valor_calculado)

# ============================ INICIANDO TESTES ================================
from random import randint
def crie_matriz(i_linhas, j_colunas, n):
    ''' (int, int, valor) -> matriz(lista de listas)
    Cria e retorna uma matriz com "i" linhas e "j" colunas
    em que cada elemento é igual ao valor dado.
    '''
    # Cria matriz vazia:
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
A = crie_matriz( 5, 30, 0) # 5 testes | 30 valores (30 dias) | entrada == 0
print('Matriz de "zeros" = lista de listas => ', A)

def imprime_matriz(A):
    n_linhas = len(A)
    n_colunas = len(A[0])
    for i in range(n_linhas):
        for j in range(n_colunas):
            T_mín = min(A[i])
            T_máx = max(A[i])
            linha = A[i][j]
        print(linha)
        

    return(T_mín, T_máx
           )
imprime_matriz(A)
    
dados_testes = []
def testa_minima(T_mín, T_máx, ):
    print('[Iniciando os testes]')
    

    
    print('[Teste finalizado]')

                
