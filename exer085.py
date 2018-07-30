n = [[], []]

for c in range(0, 7):
    nd = int(input(f'Digite {c+1}° valor: '))
    if nd % 2 == 0:
        n[0].append(nd)
    else:
        n[1].append(nd)

n[0].sort()
n[1].sort()

print(f''' > Dados:
 -Valores pares: {n[0]}
 -Valores ímpares: {n[1]}''')
