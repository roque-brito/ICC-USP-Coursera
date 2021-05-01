#screva a função remove_repetidos que recebe como parâmetro uma lista com números inteiros, v
# erifica se tal lista possui elementos repetidos e os remove. A função deve devolver uma lista 
# correspondente à primeira lista, sem elementos repetidos. A lista devolvida deve estar ordenada.
# ----------------------------------------------------------------------------------------------------
# Dica: Você pode usar lista.sort() ou sorted(lista). Qual a diferença?
# ----------------------------------------------------------------------------------------------------
# Dica: crie uma lista vazia; verifique se existe o item "i" na lista; se não hover, adicione (.append)
# ----------------------------------------------------------------------------------------------------

def remove_repetidos(l):
    lista = []                  # cria lista vazia
    for i in l:                 # para todo "i" na lista "l"
        if i not in lista:      # se o numero não estiver na lista
            lista.append(i)     # adiciona o numero "i" a lista vazia "lista"
    lista.sort()                # ordena a lista em ordem crescente
    
    return lista


