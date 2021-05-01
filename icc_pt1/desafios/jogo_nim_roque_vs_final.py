 # Desafio: Jogo NIM
 # n = n° de peças inicial
 # m = n° máximo de peças que é possível retirar em uma jogada
 # se n é multiplo de m+1, jogador começa ("Você começa!") caso contrario, "Computador começa!" (Ok)
 # Estratégia do computador: deixar sempre um n° de peças que seja multiplo de m+1 ao jogador, caso não seja possível, o comp. retira todas as peças possíveis
 # Implementar a estratégia do computador
 # -----------------------------------------------------------------------------------------------------------------------------------------------------------
from time import sleep
def computador_escolhe_jogada (n, m):
    k = m + 1
    cont = 0
    for i in range (1, k, 1):
        resto = n - i
        é_multiplo = (resto % k)
        if (é_multiplo == 0):
            cont += 1
            comp_retira_pç = i
    if cont == 0:
        comp_retira_pç = m
                    
    resto_pç = (n - comp_retira_pç)
    print()

    if (comp_retira_pç > 1):
        print('O computador tirou {} peças'.format(comp_retira_pç))
    else:
        print('O computador tirou uma peça.')

    if (resto_pç > 1):
        print('Agora restam {} peças no tabuleiro.'.format(resto_pç))
    elif resto_pç == 0:
        return(comp_retira_pç)
    else:
        print('Agora resta apenas uma peça no tabuleiro.')
    
    return (comp_retira_pç)
# ----------------------------------------------------------------------------------------------------
def usuario_escolhe_jogada (n, m):
    print('')
    user_retira_pç = int(input('Quantas peças você vai tirar? ' ))
    print()
    if (user_retira_pç > m):
        while user_retira_pç > m:
            print('Oops! Jogada inválida! Tente de novo.')
            user_retira_pç = int(input('Quantas peças você vai tirar? ' ))
            print()

    if (user_retira_pç > n):
        while user_retira_pç > n:
            print('Oops! Jogada inválida! Tente de novo.')
            user_retira_pç = int(input('Quantas peças você vai tirar? ' ))
            print()
    
    if (user_retira_pç <= 0):
        while (user_retira_pç <= 0):
            print('Oops! Jogada inválida! Tente de novo.')
            user_retira_pç = int(input('Quantas peças você quer retirar? ' ))
            print()
    
        while (user_retira_pç <= 0):
            print('Oops! Jogada inválida! Tente de novo.')
            user_retira_pç = int(input('Quantas peças você quer retirar? ' ))
            print()
    
    if user_retira_pç == 1:
        print('Você tirou uma peça.')
    else:
        print('Você tirou {} peças.'.format(user_retira_pç))
    us_resto_pç = (n - user_retira_pç)
    if (us_resto_pç == 1):
        print('Agora resta apenas uma peça no tabuleiro. ')
    else:
        print('Agora restam {} peças no tabuleiro.'.format(us_resto_pç))
    sleep(1)
    return (user_retira_pç)
# ----------------------------------------------------------------------------------------------------
def partida ():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    print()
    print('PROCESSANDO...')
    sleep(1)
    if (n <= 0 or m <= 0):
        while (n <= 0 or m <= 0):
            print('Opção inválida. Digite n > 0 e m > 0')
            n = int(input('Quantas peças? '))
            m = int(input('Limite de peças por jogada? '))
            print()
                  
    k = m + 1
    é_multiplo = (n % k)
    
    if (é_multiplo == 0):
        print()
        print('Você começa!')
        c1 = 0
        c2 = 0
        while n != 0:
            n_user = usuario_escolhe_jogada(n, m)
            n = (n - n_user)
            if (n == 0):
                c1 += 1
                print('Fim do jogo! Você ganhou!')
          
            else:
                n_comp = computador_escolhe_jogada(n, m)
                n = (n - n_comp)
                if (n == 0):
                    c2 += 1
                    print('Fim de Jogo! Computador ganhou!')
  
            print()
    else:
        print('Computador começa!')
        c1 = 0
        c2 = 0
        while n != 0:
            n_comp = computador_escolhe_jogada(n, m)
            n = (n - n_comp)
            if n == 0:
                c2 += 1
                print('Fim do jogo! Computador ganhou!')

            else:
                n_user = usuario_escolhe_jogada(n, m)
                n = (n - n_user)
                if n == 0:
                    c1 += 1
                    print('Fim do jogo! Você ganhou!')
        
        print()
    return(c1, c2)

# ----------------------------------------------------------------------------------------------------
def campeonato ():
    p = partida()
  
    return(p)

# ----------------------------------------------------------------------------------------------------
def main():
    print('''
    Bem vindo ao jogo do NIM! Escolha:''')
    op = int(input('''
    1 - para jogar uma partida isolada
    2 - para jogar um campeonato '''))
    print()
    #
    # if op
    print('PROCESSANDO...')
    sleep(0.5)
    if op == 1:
        print('Vocçê escolheu uma partida isolada!')
        print()
        print('**** Rodada isolada ****')
        partida()

    else:
        print('Você escolheu um campeonato!')
        print()
        c1 = 0 # user
        c2 = 0 # comp.
        for i in range(1, 4, 1):
            print('**** Rodada {} ****'.format(i))
            print()
            v = campeonato()
            c1 += v[0]
            c2 += v[1]
        if (i == 3):
            print('**** Final do campeonato! ****')
            print()
            print('Placar: Você {} X {} Computador'.format(c1, c2))
            print()
# --------------------- INÍCIO DO JOGO ---------------------
main()


