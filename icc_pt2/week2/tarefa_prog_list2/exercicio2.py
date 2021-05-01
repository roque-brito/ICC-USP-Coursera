
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

def menor_nome(lista0):
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

    # Lista com os tamanhos de cada nome, nas mesmas posições dos nomes na lista0:
    m = min(lista1)

    # Procura na lista de tamanhos, o tamanho mais curto:
    n = lista1.index(m)

    # relaciona a o index da posição do menor tamanho ao index da posição do menor nome:
    mais_curto = lista[n]

    return mais_curto
