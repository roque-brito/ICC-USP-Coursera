# Imprime um retângulo VAZIO:
# -------------------------
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
k = 0
print('#'*(largura))
while (k < altura-2):
    k += 1
    i = 0
    print('#', end='')
    while (i < largura-2):
            print(' ', end='')
            i += 1
    print('#')
print('#'*(largura))




