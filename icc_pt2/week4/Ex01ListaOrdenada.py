
def ordenada(lista):
    ''' ordenada(lista) --> bool'''
    cont = 0
    for i in range(len(lista)):
        indice_menor = i

        # Laço para identificar os termos da lista e ordená-los caso necessário.
        for j in range(i+1, len(lista)):

            # Comparação entre os termos da lista - caso esteja desordenada if == True 
            if lista[j] < lista[indice_menor]:
                menor = lista[indice_menor]
                indice_menor = j
                cont += 1
    
    if cont == 0:
        return True
    else:
        return False
    
if __name__ == "__main__":
    # Lista aleatória com 100 termos desordenados
    lista1 = [50, 58, 51, 35, 86, 35, 96, 56, 83, 12, 
              90, 86, 70, 65, 99, 60, 92, 70, 25, 46, 
              52, 83, 44, 58, 37, 69, 90, 4, 25, 54, 
              0, 76, 20, 44, 63, 71, 35, 35, 77, 62, 
              78, 82, 34, 63, 86, 9, 60, 60, 44, 75, 
              38, 80, 62, 50, 79, 83, 6, 67, 72, 31, 
              69, 7, 77, 51, 90, 79, 45, 24, 84, 49, 
              30, 15, 43, 18, 7, 48, 59, 38, 68, 96, 
              58, 66, 8, 25, 31, 21, 55, 0, 47, 30, 
              24, 65, 47, 31, 55, 56, 90, 38, 35, 51]

    # Lista aleatória com 100 termos odenados
    lista2 = [0, 0, 4, 6, 7, 7, 8, 9, 12, 15, 18, 20, 
              21, 24, 24, 25, 25, 25, 30, 30, 31, 31, 
              31, 34, 35, 35, 35, 35, 35, 37, 38, 38, 
              38, 43, 44, 44, 44, 45, 46, 47, 47, 48, 
              49, 50, 50, 51, 51, 51, 52, 54, 55, 55, 
              56, 56, 58, 58, 58, 59, 60, 60, 60, 62, 
              62, 63, 63, 65, 65, 66, 67, 68, 69, 69, 
              70, 70, 71, 72, 75, 76, 77, 77, 78, 79, 
              79, 80, 82, 83, 83, 83, 84, 86, 86, 86, 
              90, 90, 90, 90, 92, 96, 96, 99]    
    
    x = ordenada(lista2)
    print(x)