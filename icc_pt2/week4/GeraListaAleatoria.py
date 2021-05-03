
def ListaAleatoria(intervalo_inicial, intervalo_final):
    ''' ListaAleatoria(int, int) --> list '''

    from random import randint
    
    lista = []
    for i in range(intervalo_inicial, intervalo_final):
        num = randint(intervalo_inicial, intervalo_final)
        lista.append(num)
    
    return lista


    
if __name__ == '__main__':
    
    lista = ListaAleatoria(0, 1000)
    print(lista)
