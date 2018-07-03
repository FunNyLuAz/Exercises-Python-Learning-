#Método Matemático
print('{:=^30}'.format('[BANCO]'))

n = int(input('Digite o valor a ser sacado: R$'))

n50 = n//50
n20 = (n % 50)//20
n10 = ((n % 50) % 20)//10
n1 = n % 10

print(f'Você receberá:')

if n50 != 0:
    print(f'{n50} nota(s) de R$50')
if n20 != 0:
    print(f'{n20} nota(s) de R$20')
if n10 != 0:
    print(f'{n10} nota(s) de R$10')
if n1 != 0:
    print(f'{n1} nota(s) de R$1')

#Usando o while True
'''n = int(input('Digite o valor a ser sacado: R$'))
t = n
c = 50
tc = 0

print(f'Você receberá:')
while True:
    if t >= c:
        t -= c
        tc += 1
    else:
        if tc > 0:
            print(f'{tc} nota(s) de R${c}')
        if c == 50:
            c = 20
        elif c == 20:
            c = 10
        elif c == 10:
            c = 1
        tc = 0
        if t == 0:
            break'''
