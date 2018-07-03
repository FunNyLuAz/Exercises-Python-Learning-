from random import randint
from time import sleep

print('Tente advinhar que número eu pensei, ele está entre 0 e 10')

nr = randint(0, 10)
ni = -1
tt = 0

while not nr == ni:
    ni = int(input('> Qual é o número?: \n'))
    tt += 1
    if ni == nr:
        print('Parabéns, você acertou!')
    elif ni < nr:
        print('Você errou, tente um número maior')
    elif ni > nr:
        print('Você errou, tente um número menor')

print('\nPROCESSANDO...')
sleep(0.7)
print('Você acertou em {} tentativas'.format(tt))
