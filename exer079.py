ni = []

while True:
    n = int(input(' > Digite um valor: \n'))
    if n not in ni:
        ni.append(n)
        print('-Valor adicionado com sucesso')
    else:
        print('-Valor já existente')
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]: ').upper()[0]
    if r == 'N':
        break
    print('')

print('\nVocê digitou os valores: ',end='')
for p, c in enumerate(sorted(ni)):
    if p != len(ni)-1:
        print(c, end=' - ')
    else:
        print(c)
