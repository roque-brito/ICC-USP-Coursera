# Caracteres maiúsculos na tabela ASCII em DEC: 65 = A, 66 = B, ..., 90 = Z.
# =========================================================================

def maiusculas(frase):
    letras = ''
    alfabeto_maiusculo = []
    for i in range(65, 91):
        alfabeto_maiusculo.append(chr(i))
    
    for j in range(len(frase)):
        letra = frase[j]
        if letra in alfabeto_maiusculo:
            letras += letra
        
    return letras

# Função para testar o código:
'''
def testa_maiusculas():
    frase1 = 'Programamos em python 2?'
    frase2 = 'Programamos em Python 3?'
    frase3 = 'Cada Agasalho Foi Esquecido'
    frase4 = 'PrOgRaMaMoS em python!'

    print('='*50)

    t1 = maiusculas(frase1)
    if t1 == 'P':
        print('CÓDIGO PASSOU NO TESTE 1')
        print('Resultado esperado: P')
        print(f'Resultado devolvido: {t1}')
    else:
        print('CÓDIGO FALHOU NO TESTE 1')
        print('Resultado esperado: P')
        print(f'Resultado devolvido: {t1}')

    print('='*50)

    t2 = maiusculas(frase2)
    if t2 == 'PP':
        print('CÓDIGO PASSOU NO TESTE 2')
        print('Resultado esperado: PP')
        print(f'Resultado devolvido: {t2}')
    else:
        print('CÓDIGO FALHOU NO TESTE 2')
        print('Resultado esperado: PP')
        print(f'Resultado devolvido: {t2}')

    print('='*50)

    t3 = maiusculas(frase3)
    if t3 == 'CAFE':
        print('CÓDIGO PASSOU NO TESTE 3')
        print('Resultado esperado: CAFE')
        print(f'Resultado devolvido: {t3}')
    else:
        print('CÓDIGO FALHOU NO TESTE 3')
        print('Resultado esperado: CAFE')
        print(f'Resultado devolvido: {t3}')

    print('='*50)

    t4 = maiusculas(frase4)
    if t4 == 'PORMMS':
        print('CÓDIGO PASSOU NO TESTE 4')
        print('Resultado esperado: PORMMS')
        print(f'Resultado devolvido: {t4}')
    else:
        print('CÓDIGO FALHOU NO TESTE 4')
        print('Resultado esperado: PORMMS')
        print(f'Resultado devolvido: {t4}')

    print('='*50)

# =========================    
testa_maiusculas()        
# =========================    
'''    
    
    
