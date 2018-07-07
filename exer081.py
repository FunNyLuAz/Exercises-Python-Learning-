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
for c in sorted(nn, reverse=True):
    if c != sorted(nn, reverse=True)[len(nn)-1]:
        od += f'{c} - '
    else:
        od += f'{c}'

print(f'''\n > Dados: 
 -Quantidade de valores: {len(nn)}
 -Ordem decrescente: {od}
 -O valor 5 {n5[0] if (5 in nn) is True else n5[1]} na lista acima''')
