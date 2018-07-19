p = []
i = []

n = [p, i]

for c in range(0, 7):
    nd = int(input('Digite um valor: '))
    if nd % 2 == 0:
        p.append(nd)
    else:
        i.append(nd)

n[0].sort()
n[1].sort()

print(f''' > Dados:
 -Valores pares: {n[0]}
 -Valores ímpares: {n[1]}''')
