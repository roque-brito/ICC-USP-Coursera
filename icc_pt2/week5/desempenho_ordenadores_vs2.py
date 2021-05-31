from time import time
from random import randrange
import ordenador

class ContaTempos:

    def lista_aleatoria(self, n):
        lista = [randrange(1000) for x in range(n)]
        return lista

    def lista_quase_ordenada(self, n):
        lista = [x for x in range(n)]
        lista[n // 10] = -500
        return lista

    def compara(self, n):
        lista1 = self.lista_aleatoria(n)
        lista2 = lista1[:]  # lista1 foi "clonada"

        ordena = ordenador.Ordenador()

        print('-='*17)
        print('Comparação 1 | listas aleatórias:')
        # ---------------- Ordenador Bubble-Quick ----------------------
        print('-='*17)
        t_inicial = time()
        ordena.bolha_quick(lista1)
        t_final = time()
        delta_t1 = t_final - t_inicial
        
        if delta_t1 > 60:
            delta_t1 = delta_t1 / 60
            print(f'Ordenador BubbleSort-Quick demorou {delta_t1:.4} minutos')

        print(f'Ordenador BubbleSort-Quick demorou {delta_t1:.4} segundos')

        # ---------------- Ordenador Seleção-Direta -------------------
        t_inicial = time()
        ordena.selecao_direta(lista2)
        t_final = time()
        delta_t2 = t_final - t_inicial
        
        if delta_t2 > 60:
            delta_t2 = delta_t2 / 60
            print(f'Ordenador Seleção_Direta demorou {delta_t2:.4} minutos')

        print(f'\nOrdenador Seleção_Direta demorou {t_final - t_inicial:.4} segundos')
        print('-'*100)

        # ---------------- Verificação --------------------------------
        fator = delta_t1 / delta_t2
        if delta_t1 < delta_t2:
            
            print(f'Para listas aleatórias, o algoritmo BubbleSort-Quick é {fator:.2} vezes mais rápido que Seleção_Direta')
        else:
            print(f'Para listas aleatórias, o algoritmo Seleção_Direta é {fator:.2} vezes mais rápido que BubbleSort-Quick')
        
        print('_'*100)

        # ======================================= comparação 2 =======================================
        print('-='*17)
        print('Comparação 2 | listas Quase-Ordenadas:')
        # ---------------- Ordenador Bubble-Quick ----------------------
        print('-='*17)
        lista1 = self.lista_quase_ordenada(n)
        lista2 = lista1[:]

        t_inicial = time()
        ordena.bolha_quick(lista1)
        t_final = time()
        delta_t1 = t_final - t_inicial
        
        if delta_t1 > 60:
            delta_t1 = delta_t1 / 60
            print(f'Ordenador BubbleSort-Quick demorou {delta_t1:.4} minutos')

        print(f'Ordenador BubbleSort-Quick demorou {delta_t1:.4} segundos')

        # ---------------- Ordenador Seleção-Direta -------------------
        t_inicial = time()
        ordena.selecao_direta(lista2)
        t_final = time()
        delta_t2 = t_final - t_inicial
        
        if delta_t2 > 60:
            delta_t2 = delta_t2 / 60
            print(f'Ordenador Seleção_Direta demorou {delta_t2:.4} minutos')

        print(f'\nOrdenador Seleção_Direta demorou {t_final - t_inicial:.4} segundos')
        print('-'*100)

        # ---------------- Verificação --------------------------------
        fator = delta_t1 / delta_t2
        if delta_t1 < delta_t2:
            
            print(f'Para listas Quase-Ordenadas, o algoritmo BubbleSort-Quick é {fator:.2} vezes mais rápido que Seleção_Direta')
        else:
            print(f'Para listas Quase-Ordenadas, o algoritmo Seleção_Direta é {fator:.2} vezes mais rápido que BubbleSort-Quick')
        
        print('_'*100)

        
# ------------ TESTE ------------
if __name__ == '__main__':
    c = ContaTempos()
    c.compara(5000)
    #print(c.lista_quase_ordenada(100))
    