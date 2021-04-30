print('-'*50)
print('Este programa calcula o Fatorial de qualquer número.')
n = int(input('Digite um número: '))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))