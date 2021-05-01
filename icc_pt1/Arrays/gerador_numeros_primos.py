# -------------------------
# GERADOR DE NÚMEROS PRIMOS
# -------------------------
def éPrimo(x):
    fat = 2
    if x == 2:
        return True

    while ((x % fat != 0) and (fat <= x/2)):
        fat += 1
    if x % fat == 0:
        return False
    else:
        return True

lim = int(input('Limite = '))

n = 2
while n < lim:
    if éPrimo(n):
        print(n, end=', ')
    n += 1
