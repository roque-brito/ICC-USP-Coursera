# Binomio de Newton: implemetando uma função para o cálculo do fatorial
# ---------------------------------------------------------------------
# -------------- FUNÇÃO PARA CALCULAR O FATORIAL ----------------------
def fatorial (n):
    f = 1
    while n > 0:
        f *= n
        n -= 1
    return(f)
# -------------- FUNÇÃO PARA CALCULAR O BINÔMIO -----------------------
def binomial (x, y):
    return (fatorial(N) / (fatorial(k) * fatorial(N - k)))
# ---------------------------------------------------------------------
print('''
# ------------------------------------------------
Calculando a análise combinatória de dois números. 
O cálculo consiste no número de combinações de "n" 
termos de tamanho "k" de "k" em "k"
# ------------------------------------------------
''')
N = int(input('Digite um número inteiro: N = '))
k = int(input('Digite um número inteiro: k = '))
b = binomial(N, k)
print(b)