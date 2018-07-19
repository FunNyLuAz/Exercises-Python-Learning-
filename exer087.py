n = []
cl = -1
cc = sp = s3 = m2 = 0

for c in range(0, 9):
    cl += 1
    if cl == 3:
        cl = 0
        cc += 1
    n.append(int(input(f'Digite um valor para a Posição ({cc},{cl}): ')))
    if n[c] % 2 == 0:
        sp += n[c]
    if c == 2 or c == 5 or c == 8:
        s3 += n[c]

m2 = max(n[3], n[4], n[5])

print(f'\n > Matriz - 3x3 (Formatada):')
for p, c in enumerate(n):
    if (p != 3) and (p != 6):
        print(f'[{f"{c}":^3}]', end=' ')
    else:
        print(f'\n[{f"{c}":^3}]', end=' ')

print(f'''\n\n > Dados:
 -Soma dos valores pares: {sp}
 -Soma dos valores da 3ª Coluna: {s3}
 -O maior valor da 2ª Linha: {m2}''')
