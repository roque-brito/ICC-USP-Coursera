# Reescreva a função 'maximo' do outro exercício,
# que devolve o maior valor dentre dois inteiros recebidos,
# para que ela passe a receber 3 valores inteiros como parâmetros e
# devolva o maior dentre eles.
# -----------------------------------------------------------------
def maximo (x, y, z):
    
    if (y > x and y > z):
        maximo = y
    elif (z > x and z > y):
        maximo = z
    elif (x > y and x > z):
        maximo = x
       
    else:
        maximo = x
    return maximo
