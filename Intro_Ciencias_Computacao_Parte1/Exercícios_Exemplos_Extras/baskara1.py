# função do 2° grau: cálculo das raízes de uma função de grau 2 univariada:
# ------------------------------------------------------------------------
from math import sqrt

def main():
    a = float(input('Digite o valor de a: '))
    b = float(input('Digite o valor de b: '))
    c = float(input('Digite o valor de c: '))
    raizes(a, b, c)

def delta (a, b, c):
    return ((b ** 2) - (4 * a * c))


def raizes (a, b, c):
    D = delta(a, b, c) 
    if  (D == 0):
        r1 = (-b + sqrt(D)) / (2 * a)
        print('A única raíz é {}'.format(r1))
    
    elif (D > 0):
        r1 = (-b + sqrt(D)) / (2 * a)
        r2 = (-b - sqrt(D)) / (2 * a)
        print('As raízes dessa função são r1 = {:.2f} e r2 = {:.2f}'.format(r1, r2))
    else:
        print('Esta função não possui raízes reais')
    print('='*35)

main()
