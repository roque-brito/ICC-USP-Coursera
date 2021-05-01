# Escreva uma função que recebe um array de strings como parâmetro e devolve o primeiro string na ordem lexicográfica, ignorando-se
# letras maiúsculas e minúsculas.
# *** lexicografia compara código Unicode
# =================================================================================================================================
def primeiro_lex(lista):
    ''' Essa função recebe um array de strings e devolve o primeiro string na ordem lexicográfica (considerando MAIÚSCULA/minúscula)'''
    primeiro = lista[0] #define o primeiro como menor sring;

    for i in range(len(lista)):
        elemento_string = lista[i]
        
        if elemento_string < primeiro:
            primeiro = elemento_string

    print(primeiro)

    return primeiro


def testa_menor_string():
    teste_01 = ['AAAAAA', 'b']
    saida_teste = primeiro_lex(teste_01)
    if saida_teste == 'AAAAAA':
        print(f'TESTE 1: CÓDIGO FUNCIONOU. Esperado: {teste_01[0]}; Recebido: {saida_teste}')
    else:
        print(f'TESTE 1: CÓDIGO NÃO FUNCIONOU. Esperado: {teste_01[0]}; Recebido: {saida_teste}')
    
    # ==============================================================================================
    teste_02 = ['oĺá', 'A', 'a', 'casa']
    saida_teste = primeiro_lex(teste_02)
    if saida_teste == 'A':
        print(f'TESTE 2: CÓDIGO FUNCIONOU. Esperado: {teste_02[1]}; Recebido: {saida_teste}')
    else:
        print(f'TESTE 2: CÓDIGO NÃO FUNCIONOU. Esperado: {teste_02[1]}; Recebido: {saida_teste}')
    

    pass
    return

testa_menor_string()