# Escreva o seu programa

def main():
    n = int(input('Digite um número inteiro: '))
    while n > 0:
        m = 1
        c = 0
        while m < n+1:
            if (n % m == 0):
                c += 1
            m += 1
        if (c == 2): 
            print('O número {} é primo'.format(n))
        else:
            print('O numero', n, 'não é primo')
        n -= 1 
        
        

#-----------------------------------------------------
main() # chamada da funcao principal