# Usuário digita um número (int) e devolve o fatorial, dentro de um laço:
# -----------------------------------------------------------------------
def man():
    from time import sleep
    num = 1
    while num != 0:
        print('-'*30)
        num = int(input('Digite um número inteiro: '))
        f = 1
        cont = 0
        while num > 0:
            f *= num
            num -= 1
            cont += 1
        print('{:.1f}! = {}'.format(cont, f))
        print('-'*30)
        num = int(input('Digite [0] para sair ou [1] para continuar: '))
        if num == 0:
            print('Finalizando programa...')
            sleep(1)
            print('-'*30)

    return(f)

man()