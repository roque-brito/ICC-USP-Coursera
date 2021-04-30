# Módulo Sequência de Fibonacci
# Exemplo extraído da documentação oficial do Python 3
# ========================================================

def fib(n):     # escreve na tela a sequencia de Fibonacci até um número n (dado)
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a+b
    print()

def fib2(n):    # retorna a sequencia de Fibonacci até o numero n
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a+b
    return result

if __name__ == '__main__':
    import sys      # modulo sys permite interagir co o sistema operaciona
    fib(int(sys.argv[1]))
    