p = ('COMPUTADOR', 'JOGO', 'TECLADO', 'MOUSE', 'ESPADA',
     'NINTENDO', 'SWITCH', 'ZELDA', 'CELULAR', 'CASE')

for c in p:
    print(f'\033[1;34m > Em \033[4;32m{c}\033[1;34m temos as seguintes vogais: ', end='')
    for ct, l in enumerate(c):
        if l in 'AEIOU':
            print(f'\033[1;32m{l}', end=' ')
    print('\n')
