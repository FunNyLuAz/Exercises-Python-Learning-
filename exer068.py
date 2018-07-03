from random import randint
v = 0
jv = ['\033[4mpar\033[m', '\033[4mímpar\033[m']

while True:
    pi = ' '
    n = -1
    while pi not in 'PI':
        pi = input(' > Par ou Ímpar? [P/I]: \n').strip().upper()[0]
    while not 0 <= n <= 10:
        n = int(input(' > Escolha sua jogada: \n'))
    nr = randint(0, 10)
    if (((n + nr) % 2 == 0) and (pi in 'P')) or (((n + nr) % 2 != 0) and (pi in 'I')):
        print(f'''-Parabéns você venceu
-O computador jogou {nr}
-Resultando no número {nr+n} ({jv[0] if pi in 'P' else jv[1]})\n''')
        v += 1
        print('Quero revanche...')
    else:
        print(f'''-GAME OVER!
-Você perdeu depois de ganhar {v} vez(es)
-O computador jogou {nr}
-Resultando no número {nr+n} ({jv[0] if ((n + nr) % 2 == 0) else jv[1]})''')
        break
