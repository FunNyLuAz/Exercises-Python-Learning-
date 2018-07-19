from random import randint
from time import sleep

print(f'{"< Gerador de Palpites >":-^31}')

q = int(input('Quantidade de palpites: '))
p = []
c = ct = nr = 0

print('PROCESSANDO...\n')
sleep(0.7)

while not c == q:
    while ct != 6:
        nr = randint(1, 60)
        if nr not in p:
            p.append(nr)
        else:
            ct -= 1
        ct += 1
    p.sort()
    print(f'{c+1}º Palpite: {p}')
    p.clear()
    ct = 0
    c += 1
