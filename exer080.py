nd = []

for c in range(0, 5):
    n = int(input(f' > Digite o {c+1}º valor: '))
    if c == 0 or n > nd[-1]:
        nd.append(n)
        print(f' -Valor adicionado à ÚLTIMA Posição')
    else:
        p = 0
        while p < len(nd):
            if n <= nd[p]:
                nd.insert(p, n)
                print(f' -Valor adicionado à {p+1}ª Posição')
                break
            p += 1

print('\n > Valores digitados: ')
for p, c in enumerate(nd):
    if p == len(nd)-1:
        print(c)
    else:
        print(c, end=' - ')
