nn = []
n5 = ['está', 'não está']
od = ''

while True:
    nn.append(int(input(' > Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':
        break

print('\n > Você digitou os seguintes números: ')
for c in nn:
    print(f'{c} - ' if c != nn[-1] else f'{c}', end='')

nn.sort(reverse=True)
for c in nn:
    od += f'{c} - ' if c != nn[-1] else f'{c}'

print(f'''\n\n > Dados: 
 -Quantidade de valores: {len(nn)}
 -Ordem decrescente: {od}
 -O valor 5 {n5[0] if (5 in nn) is True else n5[1]} na lista acima''')
