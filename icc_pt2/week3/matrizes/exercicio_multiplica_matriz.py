import matriz
def produto_matriz(A, B):
    num_linhas = len(A)     # número de linhas da matriz A
    num_colunas = len(B[0]) # número de colunas da matriz B
    assert num_linhas == num_colunas # devolve erro se a condição não for verdadeira
    
    # Criando uma matriz com num_linhas(A) = num_colunas(B):   
    C = matriz.cria_matriz(num_linhas, num_colunas, elemento=0)
    
    # Definindo contadores: 
    k = A[0]    # Número de colunas de (A): para percorrer cada termo da linha de A
    
    # Contadores iniciais para armazenar cada novo elemento da matriz C
    i = 0   # usar para adicionar nova linha
        
    for lin in range(num_linhas):
        j = 0   # zerar a cada nova linha
        for col in range(num_colunas):

            # laço para percorrer cada elemento da linha de A e cada elemento da coluna de B,
            for l in range(len(k)):         

                # multiplicando os elementose somando o resultado
                C[i][j] += A[i][l] * B[l][j]
            
            j += 1
        i += 1
    return C

if __name__ == '__main__':
    A = [[3, 2, 1], 
         [3, 2, 1], 
         [3, 2, 1], 
         [3, 2, 1]
        ]
    B = [[10, 10, 10, 10],
         [20, 20, 20, 20],
         [30, 30, 30, 30],
        ]

    '''
    A = [[1, 2, 3],
         [4, 5, 6]
        ]
    
    B = [[1, 2],
         [3, 4],
         [5, 6]
        ]
    
    A = [[3, 2, 1], 
         [3, 2, 1], 
         [3, 2, 1], 
         ]
    B = [[10, 10, 10, 10],
         [20, 20, 20, 20],
         [30, 30, 30, 30],
        ]
    '''
    print(produto_matriz(A, B))

