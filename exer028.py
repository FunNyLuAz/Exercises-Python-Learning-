import random
import time
print('Tente advinhar que número eu pensei, ele está entre 0 e 5')
nr = random.randint(0, 5)
ni = int(input('Qual é o número?: '))
print('PROCESSANDO...')
time.sleep(0.7)
if ni == nr:
    print('Parabéns, você acertou!')
else:
    print('Não foi desta vez, eu pensei no número', nr)
