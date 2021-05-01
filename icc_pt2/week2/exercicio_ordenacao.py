from operator import itemgetter, attrgetter
lista = ['carlos  ', 'antônio  ', 'cleberson', '   Lú   ', 'alzira',  ' roberto']

def formata(lista):
    ''' ========================================================================================
    Essa função formata a lista: extrai espaços vazios e formata a primeira letra para maiúscula.
    Entrada: lista de strings
    Saída: lista de strings
    ========================================================================================''' 
    lista_formatada = []
    for i in range(len(lista)):
        nome = str(lista[i]).strip().capitalize()
        l = len(nome)
        lista_formatada.append(nome)
    
    return lista_formatada

def nome_mais_curto(lista0):
    ''' ========================================================================================
    Essa função cria uma nova lista com os tamanhos de cada nome; encontra o valor mínimo e busca 
    o índice desse valor mínimo na lista principal (ja formatada); a seguir, ela imprime o nome 
    associado ao índice do nome mais curto.
    Entada: lista formatada
    Saída: string com nome mais curto
    ========================================================================================'''
    lista = formata(lista0)
    lista1 = []
    for i in range(len(lista)):
        nome = lista[i]
        tam_nome = len(nome)
        lista1.append(tam_nome)
    m = min(lista1)
    n = lista1.index(m)
    mais_curto = lista[n]

    return mais_curto

# --------------------------------- TESTE AUTOMATIZADO ---------------------------------
def testa_nome_mais_curto():
    # teste 1
    lista1 = [' anderson  ', '  ana ', 'juca', ' roque']
    nome1 = nome_mais_curto(lista1)
    print('-'*100)
    
    if nome1 == 'Ana':
        print('CÓDIGO PASSOU NO TESTE [1]: OKAY')
        print(f'{nome1}')
    else:
        print(f''' CÓDIGO NÃO PASSOU NO TESTE [1]:
        lista1 = [' anderson  ', '  ana ', 'juca', ' roque']
        Nome esperado: 'Ana'
        Nome recebido: {nome1}''')

    lista2 = ['carlos  ', 'antônio  ', '   Lú   ', 'alzira',  ' roberto']
    nome2 = nome_mais_curto(lista2)
    print('-'*100)

    if nome2 == 'Lú':
        print('CÓDIGO PASSOU NO TESTE [2]: OKAY')
        print(f'{nome2}')
    else:
        print(f''' CÓDIGO NÃO PASSOU NO TESTE [2]:
        lista2 = ['carlos  ', 'antônio  ', '   Lú   ', 'alzira',  ' roberto']
        Nome esperado: 'Lú'
        Nome recebido: {nome2}''')

    lista3 = ['Fernanda','Luana','Helly','durval','dimas','caco']
    nome3 = nome_mais_curto(lista3)
    print('-'*100)
    
    if nome3 == 'Caco':
        print('CÓDIGO PASSOU NO TESTE [3]: OKAY')
        print(f'{nome3}')
    else:
        print(f''' CÓDIGO NÃO PASSOU NO TESTE [3]:
        lista3 = ['Fernanda','Luana','Helly','durval','dimas','caco']
        Nome esperado: 'Caco'
        Nome recebido: {nome3}''')

    lista4 = ['Fernanda','Luana','Helly','durval','dimas','     ã     ', 'caco']
    nome4 = nome_mais_curto(lista4)
    print('-'*100)
    
    if nome4 == 'Ã':
        print('CÓDIGO PASSOU NO TESTE [4]: OKAY')
        print(f'{nome4}')
    else:
        print(f''' CÓDIGO NÃO PASSOU NO TESTE [4]:
        lista3 = ['Fernanda','Luana','Helly','durval','dimas','     ã     ', 'caco']
        Nome esperado: 'Caco'
        Nome recebido: {nome4}''')

    return
testa_nome_mais_curto()
