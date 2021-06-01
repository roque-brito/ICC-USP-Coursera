def busca_binaria(lista, elemento, min=0, max=None):
    if max == None:
        max = len(lista) - 1

    if max < min:
        return False
    else:
        meio = min + ((max - min) // 2)
    
    if lista[meio] > elemento:
        return busca_binaria(lista, elemento, min, (meio-1))
    
    elif lista[meio] < elemento:
        return busca_binaria(lista, elemento, (meio+1), max)
    
    else:
        return meio

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

import pytest

@ pytest.mark.parametrize("lista, valor, esperado", [
    (l, 10, 0),
    (l, 20, 1),
    (l, 30, 2),
    (l, 40, 3),
    (l, 50, 4),
    (l, 60, 5),
    (l, 70, 6),
    (l, 80, 7),
    (l, 90, 8),  
    (l, 100, 9),
    (l, 101, False),
    (l, 11, False),
    (l, 21, False),
    (l, 31, False),
    (l, 71, False)
    ])

def testa_busca_binaria(lista, valor, esperado):
    assert busca_binaria(lista, valor) == esperado
    