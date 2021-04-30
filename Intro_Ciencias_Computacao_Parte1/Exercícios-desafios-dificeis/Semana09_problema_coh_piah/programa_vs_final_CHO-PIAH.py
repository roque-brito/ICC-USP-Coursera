import re   

def le_assinatura():
    ''' A função lê os valores dos traços linguísticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print('Bem-vindo ao detector automático COH-PIAH.')
    print('Informe a assinatura típica de uma aluno infectado: ')

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    ''' A função lê todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input(f'Digite o texto [{i}] (aperte Enter para sair): ').strip()
    while texto:
        textos.append(texto)
        i += 1
        texto = input(f'Digite o texto [{i}] (aperte Enter para sair): ').strip()
    
    return textos

def separa_sentencas(texto):
    ''' A função recebe uma sentença e devolve uma lista das(com?) frases dentro da sentença'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funçao recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funçao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras que aparecem uma única vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa função recebe uma lista de palavras e devolve o número de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1
    return len(freq)
# ----------------------------------------------------------------------------------------------------------------
def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR: essa função recebe duas assinaturas de texto e deve devolver o grau de similaridade 
    nas assinaturas'''   
    grau_similaridade = 0
    for i in range(0, 6):
        similaridade = (abs(as_a[i] - as_b[i])) / 6
        grau_similaridade += similaridade
    return grau_similaridade

def calcula_assinatura(texto):
    '''IMPLEMENTAR: essa função recebe um texto e deve devolver a assinatura do texto.''' 
    # ----- traço tamanho médio (wal1) = tamanho médio das palavras / numero total de palavras:
    lista_palavras_na_frase = separa_palavras(texto)
    numero_total_palavras = len(lista_palavras_na_frase)
    tamanho_medio_palavras = 0
    for i in range(numero_total_palavras):
        retira_pontuacao = re.sub('[.,;:!?()]', '',lista_palavras_na_frase[i]) # também fuincian assim: r'[^\w\s]'
        tamanho_medio_palavras += len(retira_pontuacao)
        
    wal1 = tamanho_medio_palavras / numero_total_palavras
    
    # ----- traço Type-Token (ttr1) = n° total de palavras diferentes / n° total de palavras: 
    texto1 = re.sub('[.,;:!?()]', '', texto)
    lista_palavras = separa_palavras(texto1)
    numero_palavras = len(lista_palavras)
    num_palavras_dif = n_palavras_diferentes(lista_palavras)
    ttr1 = num_palavras_dif / numero_palavras
    
    # ----- traço Razão Hapax Legogama (hlr1) = n° de palavras únicas / n° total de palavras:
    num_palavras_unicas = n_palavras_unicas(lista_palavras)
    hlr1 = num_palavras_unicas / numero_total_palavras
    
    # ----- traço Tamanho Médio da Sentença (sal1) = soma dos n°s de caracteres em todas as sentenças / n° de sentenças
    sentencas = separa_sentencas(texto)
    char_sentenca = 0
    numero_sentencas = len(sentencas)

    for i in range(len(sentencas)):
        sentenca = sentencas[i]
        sentenca.strip()
        char_sentenca += len(sentenca)

    sal1 = char_sentenca / numero_sentencas

    # ----- traço Complexidade de sentença (sac1) = n° de frases / n° total de sentenças:
    '''frases = separa_frases(texto)
    numero_frases = len(frases)
    sac1 = numero_frases / numero_sentencas'''
    sentencas = separa_sentencas(texto)
    n_frases = 0
    for i in range(len(sentencas)):
        frases = separa_frases(sentencas[i])
        n_frases += len(frases)
    sac1 = n_frases / len(sentencas)

    # ---- traço Tamanho médio de frase = soma do n° de caracteres de cada frase / n° de frases no texto
    sentencas = separa_sentencas(texto)
    cont_frases = 0
    char_frase = 0
    for i in range(len(sentencas)):
        frases = separa_frases(sentencas[i])
        cont_frases += len(frases)
        for j in range(len(frases)):
            char_frase += len(frases[j])

        pal1 = char_frase / cont_frases

    pal1 = char_frase / cont_frases

    assinaturas = [wal1, ttr1, hlr1, sal1, sac1, pal1]
    return(assinaturas)

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR: essa função recebe uma lista de textos e uma assinatura ass_cp e deve devolver o número (1 a n) do texto
    com maior probabilidade de ter sido infectado por COH-PIAH'''
    j = 1
    ass_b = calcula_assinatura(textos[j])
    S = compara_assinatura(ass_cp, ass_b)    # S = Similaridade entre assinaturas cp (infectado) e b (textos de entrada)
    similaridade_menor = S
    n = 0
    for i in range(len(textos)):
        ass_b = calcula_assinatura(textos[i])
        S = compara_assinatura(ass_cp, ass_b)   
        print(f"SIMILARIDADE [{i+1}] = {S}")
        if S <= similaridade_menor:
            n = i+1
            similaridade_menor = S
    print(f'O autor do texto {n} está infectado por COH-PIAH')
    return(n)

def main():
    ass_cp = le_assinatura()
    textos = le_textos()
    avalia_textos(textos, ass_cp)

main()
    



