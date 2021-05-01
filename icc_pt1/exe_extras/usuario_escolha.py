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

    return (user_retira_pç)
