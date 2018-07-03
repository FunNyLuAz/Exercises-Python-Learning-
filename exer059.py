from time import sleep

n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))

op = 0

while op != 5:
    op = int(input('''
[ 1 ] Somar os valores
[ 2 ] Multiplicar os valores
[ 3 ] Descobrir o maior valor
[ 4 ] Digitar outros valores
[ 5 ] Encerrar programa

> Escolha uma opção:\n '''))

    if op == 1:
        nr = n1+n2
        print('A soma dos valores resulta em {}'.format(nr))
    elif op == 2:
        nr = n1*n2
        print('A multiplicação dos valores resulta em {}'.format(nr))
    elif op == 3:
        nr = max(n1, n2)
        print('O maior valor é {}'.format(nr))
    elif op == 4:
        print('\nREINICIANDO...')
        sleep(0.4)
        n1 = int(input('Digite o valor 1: '))
        n2 = int(input('Digite o valor 2: '))
    elif op == 5:
        print('\nENCERRANDO...')
        sleep(0.4)
    else:
        print('Opção Inválida, tente novamente')
