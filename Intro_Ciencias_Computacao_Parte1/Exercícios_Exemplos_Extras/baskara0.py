import math
# ----------------------------------------
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
print('-'*40)
delta = (b ** 2) - (4 * a * c)
print('Delta = ', delta)

if (delta == 0):
     r1 = (-b + math.sqrt(delta)) / (2 * a)
     print('A única raiz é: r = {}'.format(r1))
elif (delta < 0):
    print('Esta equação não possui raízes reais')
else:
    r1 = (-b + math.sqrt(delta)) / (2 * a)
    r2 = (-b - math.sqrt(delta)) / (2 * a)
    print('As raízes são: r1 = {} e r2 = {}'.format(r1, r2))

print('-'*40)
