from time import sleep
from random import randint
cl = {'cr': '\033[m',
      'zn': '\033[1;34m',
      'bn': '\033[1;30m',
      'rn': '\033[1;35m',
      'an': '\033[1;33m',
      'vn': '\033[1;32m',
      'mn': '\033[1;31m'}
j = int(input('{0}{1}\n'
              '{2}1 = Tesoura\n'
              '{3}2 = Papel\n'
              '{4}3 = Pedra\n'
              '{0}{1}\n'
              '{5}Escolha sua jogada: '
              .format(cl['an'], '-=-'*20, cl['zn'], cl['bn'], cl['rn'], cl['vn'])))
c = randint(1, 3)
jl = ['', 'tesoura', 'papel', 'pedra']
jpg = ((j == 1 and c == 2) or (j == 2 and c == 3) or (j == 3 and c == 1))
jpp = ((j == 1 and c == 3) or (j == 2 and c == 1) or (j == 3 and c == 2))

if j in [1, 2, 3]:
    print('PROCESSANDO...')
    sleep(0.6)
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ\n{}'.format(cl['zn']))
    sleep(0.7)
    if j == c:
        print('Empatou, nós dois jogamos {}'.format(jl[c]))
    else:
        if jpg:
            print('Parabéns você ganhou, eu joguei {}'.format(jl[c]))
        if jpp:
            print('Que pena, eu ganhei, já que eu joguei {}'.format(jl[c]))
else:
    print('{}Sua jogada é inválida'.format(cl['mn']))
