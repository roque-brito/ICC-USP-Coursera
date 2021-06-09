# Implemente a função soma_lista(lista), que recebe como parâmetro uma lista de números inteiros e devolve um número inteiro 
# correspondente à soma dos elementos desta lista. Sua solução deve ser implementada utilizando recursão.
# ==========================================================================================================================

def soma_lista(lista):
    ''' list[int, int, ...] --> int '''
    
    if len(lista) == 1:
        return lista[0]
    else:
        soma = [lista[0] + lista[1]]
        resto = lista[2:]
        nova_lista = soma + resto
        return soma_lista(nova_lista)
        
        
# -------------- TESTE --------------
if __name__ == '__main__':
    lista0 = [1]    # soma = 20
    lista1 = [1, 2, 3, 0, 4, 5, 3, 2]
    soma = soma_lista(lista1)
    print(soma)
