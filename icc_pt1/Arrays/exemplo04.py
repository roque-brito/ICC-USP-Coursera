#
primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
print(primos)
print('Termos na lista = ', len(primos))

for i in range(len(primos)):
    
    primos[i] = primos[i]**3
    print(primos[i])
    
print(primos)