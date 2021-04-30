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
        similaridade = (abs(as_a[i] - as_b[i]))
    grau_similaridade += similaridade
    return (grau_similaridade / 6)

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

# ================================= TESTES ===========================================
ass_cp = [4.325, 0.7375, 0.5875, 54.125, 2.0, 26.5625] 

textos = ['Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.', 
'Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.', 
'Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.']

def main():
    #ass_cp = le_assinatura()
    #textos = le_textos()
    avalia_textos(textos, ass_cp)

main()

    



