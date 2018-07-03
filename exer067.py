from time import sleep
cl = {'zn': '\033[1;34m',
      'an': '\033[1;33m'}

while True:
    n = int(input('Digite um número: '))
    if n < 0:
        print('Encerrando...')
        sleep(0.7)
        break
    print('-=-'*5)
    for c in range(1, 11):
        print(f'  {n} x {c:2} = {n*c}')
    print('-=-'*5)
