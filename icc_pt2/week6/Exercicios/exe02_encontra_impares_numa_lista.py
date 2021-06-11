
def encontra_impares(lista):
    ''' lista(inteiros) -> lista(inteiros ímpares) '''
    
    # Criar uma lista vazia p/ adicionar os nº ímpares:
    lista_impares = []

    # Verificar se a lista está vazia:
    if len(lista) > 0:
        
        # Verifica se o numero é par:
        if lista[0] % 2 == 0:
            
            # Remove o nº par da lista
            lista.remove(lista[0])

            # Chamada recursiva com a lista sem o número par: 
            return  encontra_impares(lista)    
        
        else:
            # Adiciona o elemeto ímpar a lista vazia:
            lista_impares.extend([lista[0]])

            # Cria uma nova lista excluindo o primeiro elemento:
            lista = lista[1:]
            
        # Atualiza a nova lista com ímpares:
        lista_impares += encontra_impares(lista)
            
    return lista_impares


# -------------- TESTE --------------
if __name__ == '__main__':
    lista0 = [0, 1]     
    lista1 = [1, 3, 2, 5, 4]
    lista2 = [1, 1, 2, 3, 4, 11, 14, 5, 3, 20, 23]
    
    lista_impares = encontra_impares(lista2)
    print(lista_impares)