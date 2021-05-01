import re
texto = 'Então resolveu ir brincar com a Máquina pra ser também imperador dos filhos da mandioca. Mas as três cunhas deram muitas risadas e falaram que isso de deuses era gorda mentira antiga, que não tinha deus não e que com a máquina ninguém não brinca porque ela mata. A máquina não era deus não, nem possuía os distintivos femininos de que o herói gostava tanto. Era feita pelos homens. Se mexia com eletricidade com fogo com água com vento com fumo, os homens aproveitando as forças da natureza. Porém jacaré acreditou? nem o herói! Se levantou na cama e com um gesto, esse sim! bem guaçu de desdém, tó! batendo o antebraço esquerdo dentro do outro dobrado, mexeu com energia a munheca direita pras três cunhas e partiu. Nesse instante, falam, ele inventou o gesto famanado de ofensa: a pacova.' 
def separa_sentencas(texto):
    ''' A função recebe uma sentença e devolve uma lista das frases dentro da sentença'''
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

# ----- codigo1 ---------------------------------------------------------------------------------
sentencas = separa_sentencas(texto)
cont_frases = 0
char_frase = 0
for i in range(len(sentencas)):
    frases = separa_frases(sentencas[i])
    cont_frases += len(frases)
    for j in range(len(frases)):
        char_frase += len(frases[j])
        
# ---- traço Tamanho médio de frase = soma do n° de caracteres de cada frase / n° de frases no texto
pal1 = char_frase / cont_frases
if pal1 != 38.5:
    print(f'ERRO: Valor de síada: {pal1} >>> valor esperado: 38.5')
else:
    print('codigo1 CORRETO =', pal1)

# Valor esperado == 38.5
