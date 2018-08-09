from random import randint
from time import sleep

print(f'{"< Gerador de Palpites >":-^31}')

q = int(input('Quantidade de palpites: '))
p = []
c = ct = 0

print('PROCESSANDO...\n')
sleep(0.7)

while not c == q:
    while ct != 6:
        nr = randint(1, 60)
        if nr not in p:
            p.append(nr)
            ct += 1
    p.sort()
    print(f'{c+1}º Palpite: {p}')
    p.clear()
    ct = 0
    c += 1

#Outra Maneira:
'''from random import randint
from time import sleep

print(f'{"< Gerador de Palpites >":-^31}')

q = int(input('Quantidade de palpites: '))
tp = []
p = []
c = ct = 0

while c < q:
    while not ct == 6:
        nr = randint(1, 60)
        if nr not in p:
            p.append(nr)
            ct += 1
    p.sort()
    tp.append(p[:])
    p.clear()
    ct = 0
    c += 1

for p, l in enumerate(tp):
    print(f'{p+1}º Palpite: {l}')
    sleep(1)

print('\nBoa sorte!')'''
