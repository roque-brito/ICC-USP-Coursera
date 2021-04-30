#screva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, v
# erifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista 
# correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
# ----------------------------------------------------------------------------------------------------
# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
# ----------------------------------------------------------------------------------------------------
# Dica: crie uma lista vazia; verifique se existe o item "i" na lista; se não hover, adicione (.append)
# ----------------------------------------------------------------------------------------------------
lista = [2, 2, 1, 13, 1, 4 , 4, 3, 5, 3, 7, 11]

def remove_repetidos(lista):
    lista.sort()
    lista_ordenada = []
    for i in lista:
        if i not in lista_ordenada:
            lista_ordenada.append(i)
    print(lista_ordenada)

    return()
seq = remove_repetidos(lista)

