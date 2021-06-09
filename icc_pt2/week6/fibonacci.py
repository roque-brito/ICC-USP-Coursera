def fibonacci(n):
    if n < 2: # BASE DA RECURSÃO
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2) # CHAMADA RECURSIVA

if __name__ =='__main__':
    fibo = fibonacci(10)
    print(fibo)

'''
import pytest
@pytest.mark.parametrize("entrada, esperado",
                         [
                             (0,0),
                             (1,1),
                             (2,1),
                             (3,2),
                             (4,3),
                             (5,5),
                             (6,8),
                             (7,13),
                             (8,21),
                             (9,34),
                            (10,55),
                         ])

def testa_fibonacci(entrada, esperado):
    assert fibonacci(entrada) == esperado
'''