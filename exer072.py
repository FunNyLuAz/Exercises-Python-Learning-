from time import sleep
ne = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
      'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
r = 'S'

while r in 'S':
    while True:
        n = int(input(' > Digite um valor [0-20]: '))
        if 0 <= n <= 20:
            break
        else:
            print('\033[1;31m -Valor inválido, tente novamente\033[m\n')

    print(f' -Você digitou o número \033[4;34m{ne[n]}\033[m\n')

    r = ' '
    while r not in 'SN':
        r = input(' > Quer continuar? [S/N]: ').upper()
    print('PROCESSANDO...\n' if r == 'S' else 'ENCERRANDO...')
    sleep(0.4)
