import re
texto = 'Essas mudanças de comportamento são implicações do processo evolutivo pelo qual estamos submetidos. Podemos ficar horas discutindo como seriam essas implicações se escolhas diferentes tivessem sido feitas. Mas penso que os resultados não seriam muito diferentes do que são. É possível afirmar que a colaboração através de grupos é da natureza humana (HARARI, 2014).   E foi através dessa colaboração antes em pequenos grupos e hoje de forma global, que desenvolvemos essa teia tecnológica que nos aprisiona aos dispositivos eletrônicos. Se antes era a fofoca em volta das fogueiras que motivava as interações, intrigas e colaborações humanas (HARARI, 2014), hoje são as mesmas fofocas incrementadas de notícias falsas em grande escala e em tempo real que ditam a pauta das atividades. A manipulação da informação é um assunto muito sério e tem tomado cada vez mais espaço das discussões acadêmicas e políticas. Esse jeito de utilizar as tecnologias atuais para interagir socialmente, consumir informação, produzir energia, revolucionar a educação, a neurociência ou a medicina, deve-se ao modo como absorvemos e processamos tudo isso. Nossa biologia nos diz para levantar e fazer exercícios, mas podemos fazê-lo numa esteira ergométrica enquanto assistimos a uma série na televisão. Se não vamos a rua ou a academia, perdemos a oportunidade de conhecer pessoas novas e interagir socialmente de modo físico (“analógico”). Mas para a sociedade atual esse pode não ser um comportamento ruim. Nesse exemplo, poderíamos nos exercitar conectados a amigos virtuais em tempo real – esses amigos poderiam nem estar no mesmo país. Após os exercícios, publica-se uma selfie numa rede social e pronto, há comentários, compartilhamentos e curtidas. Assim, socializamos.'
texto.strip()
def separa_sentencas(texto):
    ''' A função recebe uma sentença e devolve uma lista das(com?) frases dentro da sentença'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funçao recebe uma sentença e devolve uma lista das frases dentro da sentença'''
    return re.split(r'[,:;]+', sentenca)

# ----- traço Tamanho Médio da Sentença (sal1) = soma dos n°s de caracteres em todas as sentenças / n° de sentenças
sentencas = separa_sentencas(texto)
char_sentenca = 0
numero_sentencas = len(sentencas)

for i in range(len(sentencas)):
    sentenca = sentencas[i]
    sentenca.strip()
    char_sentenca += len(sentenca)

sal1 = char_sentenca / numero_sentencas

# ----- traço Complexidade de sentença (sac1) = n° de caracteres em cada frase / n° total de sentenças:
frases = separa_frases(texto)
numero_frases = len(frases)
sac1 = numero_frases / numero_sentencas # complexidade de sentença

# ---- traço Tamanho médio de frase = soma dos caracteres de cada frase / n° de frases no texto
frases = separa_frases(texto)
char_frases = 0
numero_frases = len(frases)

for j in range(len(frases)):
    frase = frases[j]
    frase.strip()
    char_frases += len(frase)
pal1 = char_frases / numero_frases


assig = [sal1, sac1, pal1]
print(assig)
