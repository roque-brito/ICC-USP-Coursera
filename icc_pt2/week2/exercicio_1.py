# Escreva uma função que recebe um array de strings como parâmetro e devolve o primeiro string na ordem lexicográfica, ignorando-se
# letras maiúsculas e minúsculas.
# *** lexicografia compara código Unicode
# =================================================================================================================================
def menor_string(meu_string):
    ''' Essa função recebe um array de strings e devolveo primeiro string na ordem lexicográfica (ignorando maiúscula/minúscula)'''
    menor_string = meu_string[0].lower() #define o primeiro como menor sring;

    for i in range(len(meu_string)):
        elemento_string = meu_string[i].lower()
        
        if elemento_string < menor_string:
            menor_string = elemento_string

    print(menor_string)

    return menor_string


def testa_menor_string():
    teste_01 = ['ana', 'maria', 'José', 'Valdemar']
    saida_teste = menor_string(teste_01)
    if saida_teste == 'ana':
        print(f'TESTE 1: CÓDIGO FUNCIONOU. Esperado: {teste_01[0].lower()}; Recebido: {saida_teste}')
    else:
        print(f'TESTE 1: CÓDIGO NÃO FUNCIONOU. Esperado: {teste_01[0].lower()}; Recebido: {saida_teste}')
    
    # ==============================================================================================
    teste_02 = ['ana', 'maria', 'Arthur', 'Bia', 'Amanda', 'anaconda']
    saida_teste = menor_string(teste_02)
    if saida_teste == 'amanda':
        print(f'TESTE 2: CÓDIGO FUNCIONOU. Esperado: {teste_02[4].lower()}; Recebido: {saida_teste}')
    else:
        print(f'TESTE 2: CÓDIGO NÃO FUNCIONOU. Esperado: {teste_02[4].lower()}; Recebido: {saida_teste}')
    
    # ==============================================================================================
    teste_03 = ['Azedo', 'Ayumi', 'Arthur', 'Acatar', 'Abmael', 'adorno']
    saida_teste = menor_string(teste_03)
    if saida_teste == 'abmael':
        print(f'TESTE 3: CÓDIGO FUNCIONOU. Esperado: {teste_03[4].lower()}; Recebido: {saida_teste}')
    else:
        print(f'TESTE 3: CÓDIGO NÃO FUNCIONOU. Esperado: {teste_03[4].lower()}; Recebido: {saida_teste}')
    
    # ==============================================================================================
    teste_04 = ['Bumbum', 'Bacon', 'barbate', 'breno', 'brinco', 'babel']
    saida_teste = menor_string(teste_04)
    if saida_teste == 'babel':
        print(f'TESTE 4: CÓDIGO FUNCIONOU. Esperado: {teste_04[5].lower()}; Recebido: {saida_teste}')
    else:
        print(f'TESTE 4: CÓDIGO NÃO FUNCIONOU. Esperado: {teste_04[5].lower()}; Recebido: {saida_teste}')
    
    # ==============================================================================================
    teste_05 = ['deda', 'dede', 'dedi', 'dedo', 'dedu']
    saida_teste = menor_string(teste_05)
    if saida_teste == 'deda':
        print(f'TESTE 5: CÓDIGO FUNCIONOU. Esperado: {teste_05[0].lower()}; Recebido: {saida_teste}')
    else:
        print(f'TESTE 5: CÓDIGO NÃO FUNCIONOU. Esperado: {teste_05[0].lower()}; Recebido: {saida_teste}')
    

    pass
    return

testa_menor_string()