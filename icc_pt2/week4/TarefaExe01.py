# Praticar tarefa de programação: exercícios adicionais
# Exercício 1: gerando listas grandes:
# =====================================================

def lista_grande(n):
    ''' (int) --> list'''
    from random import randint
    
    lista = []
    for i in range(0, n):
        num = randint(0, n)
        lista.append(num)
    
    return lista

if __name__ == '__main__':

    x = lista_grande(100)
    print(x)
