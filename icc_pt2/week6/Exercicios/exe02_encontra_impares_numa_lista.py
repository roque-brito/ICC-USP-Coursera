
def encontra_impares(lista):
    ''' lista(inteiros) -> lista(inteiros ímpares) '''
    lista_impar = []
    if ( lista[0] % 2 ) != 0:
        lista_impar.extend([lista[0]])
        return lista_impar
    else:
        lista.remove(lista[0])
        encontra_impares(lista)


    return lista_impar



# -------------- TESTE --------------
if __name__ == '__main__':
    lista0 = [0, 1]     
    lista1 = [1, 1, 2, 3, 11, 14, 5, 3, 20]
    lista_inpares = encontra_impares(lista1)
    print(lista_inpares)