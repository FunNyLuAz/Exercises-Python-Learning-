n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for l in range(0, 3):
    for c in range(0, 3):
        n[l][c] = int(input(f'Digite um valor para a Posição ({l},{c}): '))

print(f'\n > Matriz - 3x3 (Formatada):')
for l in n:
    for c in l:
        print(f'[{f"{c}":^3}]', end=' ')
    print()

#Outra Maneira
'''n = []
cl = -1
cc = 0

for c in range(0, 9):
    cl += 1
    if cl == 3:
        cl = 0
        cc += 1
    n.append(int(input(f'Digite um valor para a Posição ({cc},{cl}): ')))

print(f'\n > Matriz - 3x3 (Formatada):')
for p, c in enumerate(n):
    if (p != 3) and (p != 6):
        print(f'[{f"{c}":^3}]', end=' ')
    else:
        print(f'\n[{f"{c}":^3}]', end=' ')'''
