n = []

for c in range(0, 5):
    n.append(int(input('Digite um valor: ')))

print(' -Valores digitados: ')
for c in n:
    print(c, end=' ')

ma = [max(n)]
mi = [min(n)]

for ct, v in enumerate(n):
    if v == max(n):
        ma.append(ct)
    elif v == min(n):
        mi.append(ct)

print(f'''\n\n > Maior valor: {ma[0]}
 > Posição(ões): ''', end='')
for c in ma:
    print(f'{c} ' if c != max(n) else '', end='')

print(f'''\n\n > Menor valor: {mi[0]}
 > Posição(ões): ''', end='')
for c in mi:
    print(f'{c} ' if c != min(n) else '', end='')
