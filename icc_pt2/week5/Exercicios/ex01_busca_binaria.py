# Implemente a função busca(lista, elemento), que busca um determinado elemento em uma lista e devolve o índice correspondente à posição do elemento encontrado. 
# Utilize o algoritmo de busca binária. Nos casos em que o elemento buscado não existir na lista, a função deve devolver o booleano False.
# Além de devolver o índice correspondente à posição do elemento encontrado, a função deve imprimir cada um dos índices testados pelo algoritmo.
# ================================================================================================================================================
def busca(lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2
            print(meio)
                
            if lista[meio] == x:
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio -1
                else:
                    primeiro = meio +1
            
        return False
