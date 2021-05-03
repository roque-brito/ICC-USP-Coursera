# Praticar tarefa de programação: exercícios adicionais
# Exercício 2: ordenação com selection sort
# =====================================================

def ordena(lista):
    ''' ordena(lista) --> lista ordenada (crescente)'''
    lista1 = []
    for i in range(len(lista)):
        indice_menor = i

        for j in range(i+1, len(lista)):
            if lista[j] < lista[indice_menor]:
                menor = lista[indice_menor]
                indice_menor = j
        
        lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
    
    return lista


if __name__ == "__main__":
    lista = [50, 58, 51, 35, 86, 35, 96, 56, 83, 12, 
             90, 86, 70, 65, 99, 60, 92, 70, 25, 46, 
             52, 83, 44, 58, 37, 69, 90, 4, 25, 54, 
             0, 76, 20, 44, 63, 71, 35, 35, 77, 62, 
             78, 82, 34, 63, 86, 9, 60, 60, 44, 75, 
             38, 80, 62, 50, 79, 83, 6, 67, 72, 31, 
             69, 7, 77, 51, 90, 79, 45, 24, 84, 49, 
             30, 15, 43, 18, 7, 48, 59, 38, 68, 96, 
             58, 66, 8, 25, 31, 21, 55, 0, 47, 30, 
             24, 65, 47, 31, 55, 56, 90, 38, 35, 51]
        
    x = ordena(lista)
    print(x)