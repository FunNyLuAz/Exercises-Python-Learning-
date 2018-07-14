n = []

for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a {c+1}ª Posição: ')))

print(' -Valores digitados: ')
for c in n:
    print(c, end=' ')

ma = max(n)
mi = min(n)
'''Outra maneira:
ma = mi = 0
for c in range(0, 5):
    n.append(int(input(f'Digite um valor para a {c+1}ª Posição: ')))
    if c == 0:
        ma = mi = n[c]
    else:
        if n[c] > ma:
            ma = n[c]
        elif n[c] < mi:
            mi = n[c]'''

print(f'''\n\n > Maior valor: {ma}
 > Posição(ões): ''', end='')
for p, c in enumerate(n):
    if c == ma:
        print(f'{p} ', end='')

print(f'''\n\n > Menor valor: {mi}
 > Posição(ões): ''', end='')
for p, c in enumerate(n):
    if c == mi:
        print(f'{p} ', end='')
