# Praticar tarefa de programação: Exercícios adicionais (opcionais)
# Exercício 1 - Contando vogais ou consoantes
# ==================================================================

def conta_letras(frase, contar='vogais'):
    lista_vogais = ['a', 'e', 'i', 'o', 'u']
    lista_consoantes = []
    alfabeto = []
    n = 0
    # Formar uma lista com o alfabeto completo
    for i in range(97, 123):
        alfabeto.append(chr(i))
    
    # Formar uma lista com as consoantes: remover as vogais
    for j in range(len(alfabeto)):
        letra = alfabeto[j]
        if letra not in lista_vogais:
            lista_consoantes.append(letra)

    # contar as vogais:       
    if contar == 'vogais':
        conta_vogal = 0
        for k in range(len(frase)):
            letra_na_frase = frase[k]
            if letra_na_frase in lista_vogais:
                conta_vogal += 1
                n = conta_vogal

    # contar as consoantes:
    if contar == 'consoantes':
        conta_consoante = 0
        for l in range(len(frase)):
            letra_na_frase = frase[l]
            if letra_na_frase in lista_consoantes:
                conta_consoante += 1
                n = conta_consoante

    return n




# Teste automatizado da função:

def testa_conta_letras():
    frase1 = 'programamos em python'                                     # vogais == 06; consoantes == 13
    frase2 = 'Salada de frutas com banada, laranja, uva e abacaxi '      # vogais == 20; consoantes == 21

    #  TESTE 01
    #  testar função recebendo apenas um parâmetro: devolver numero de vogais
    print('='*50)
    n1 = conta_letras(frase1) 
    if n1 == 6:
        print('Código funciona para entrada de 1 parâmetro')
    else:
        print('Código falhou no teste de entrada para 1 parâmetro')
        print('Saída esperada: 6', f'Saída recebida: {n1}')

    #  testar função recebendo apenas o parâmetro vogal: devolver numero de vogais
    print('='*50)
    n2 = conta_letras(frase1, 'vogais') 
    if n2 == 6:
        print('Código funciona para entrada com o parâmetro "vogal"')
    else:
        print('Código falhou no teste de entrada do parâmetro "vogal"')
        print('Saída esperada: 6', f'Saída recebida: {n2}')

    #  testar função recebendo apenas o parâmetro consoante: devolver numero de consoantes
    print('='*50)
    n3 = conta_letras(frase1, 'consoantes') 
    if n3 == 13:
        print('Código funciona para entrada com o parâmetro "consoante"')
    else:
        print('Código falhou no teste de entrada do parâmetro "consoante"')
        print('Saída esperada: 13', f'Saída recebida: {n3}')

    print('='*50)
    n2 = conta_letras(frase2)
    
    print('='*50)
    return

testa_conta_letras()
    
