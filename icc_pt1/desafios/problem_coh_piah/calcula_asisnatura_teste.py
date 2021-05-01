import re   

def separa_palavras(frase):
    '''A funçao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

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

def separa_sentencas(texto):
    ''' A função recebe uma sentença e devolve uma lista das(com?) frases dentro da sentença'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funçao recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)

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

    assinaturas = [wal1, ttr1, hlr1, sal1, sac1, pal1]
    return(assinaturas)

texto = 'Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.' 
#texto = 'Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.'
assinaturas = calcula_assinatura(texto)
print(assinaturas)
