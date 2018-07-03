from emoji import emojize
from time import sleep

print('Contagem regressiva para a queima de fogos')
sleep(0.7)
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize(':fireworks:'))
