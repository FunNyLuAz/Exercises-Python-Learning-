nn = []
np = []
ni = []

while True:
    nn.append(int(input(' > Digite um valor: ')))
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':
        break

for c in nn:
    if c % 2 == 0:
        np.append(c)
    else:
        ni.append(c)

print(f'''\n > Valores digitados:
{nn}

 -Valores pares digitados:
{np}
 -Valores ímpares digitados:
{ni}''')
