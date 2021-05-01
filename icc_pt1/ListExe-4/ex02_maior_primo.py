def éPrimo (k):
    for i in range (1, k+1, 1):
        cont = 0
        for j in range (1, k+1, 1):
            resto = (i % j)
            if resto != 0:
                p = '' 
            else:
                cont += 1
        if cont == 2:
            primo = i 
    return (primo)

def maior_primo (k):
    return éPrimo(k)

k = int(input('Digite um númeo iteiro: '))
MaiorPrimo = maior_primo(k)
print(MaiorPrimo)    
