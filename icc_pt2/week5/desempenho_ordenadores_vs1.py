from time import time
from random import randrange
import ordenador

class ContaTempos:

    def lista_aleatoria(self, n):
        lista = [randrange(1000) for x in range(n)]

        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]  # lista1 foi "clonada"

        ordena = ordenador.Ordenador()

        # ---------------- Ordenador Bubble --------------------------
        print('='*50)
        t_inicial = time()
        ordena.bolha(lista1)
        t_final = time()
        delta_t1 = t_final - t_inicial
        
        if delta_t1 > 60:
            delta_t1 = delta_t1 / 60
            print(f'Ordenador BubbleSort demorou {delta_t1:.4} minutos')

        print(f'Ordenador BubbleSort demorou {delta_t1:.4} segundos')

        # ---------------- Ordenador Seleção-Direta -------------------
        t_inicial = time()
        ordena.selecao_direta(lista2)
        t_final = time()
        delta_t2 = t_final - t_inicial
        
        if delta_t2 > 60:
            delta_t2 = delta_t2 / 60
            print(f'Ordenador Seleção_Direta demorou {delta_t2:.4} minutos')

        print(f'\nOrdenador Seleção_Direta demorou {t_final - t_inicial:.4} segundos')
        print('='*100)

        # ---------------- Verificação --------------------------------
        fator = delta_t1 / delta_t2
        if delta_t1 < delta_t2:
            
            print(f'O algoritmo BubbleSort é {fator:.2} vezes mais rápido que Seleção_Direta')
        else:
            print(f'O algoritmo Seleção_Direta é {fator:.2} vezes mais rápido que BubbleSort')
        
        print('='*100)

# ------------ TESTE ------------
if __name__ == '__main__':
    c = ContaTempos()
    c.compara(1000)
    