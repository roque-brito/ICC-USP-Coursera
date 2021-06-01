class Ordenador:
    def selecao_direta(self, lista):
        ''' (self, list) --> list'''
        
        fim = len(lista)

        for i in range(fim - 1):
            # Defina o primeiro elemento como o menor i-ésimo:
            posicao_minimo = i

            for j in range(i+1, fim):
                if lista [j] < lista[posicao_minimo]:
                    posicao_minimo = j
            
            # Troque a posição dos elementos de lugar na lista:
            lista[i], lista[posicao_minimo] = lista[posicao_minimo], lista[i]

    def bolha(self, lista):
        ''' (self, list) --> list'''
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
        return lista

    def bolha_quick(self, lista):
        ''' (self, list) --> list'''
        fim = len(lista)

        for i in range(fim-1, 0, -1):
            trocou_termo = False
            for j in range(i):
                if lista[j] > lista[j+1]:
                    lista[j], lista[j+1] = lista[j+1], lista[j]
                    trocou_termo = True
            
            if not trocou_termo:
                return lista

        return lista 








