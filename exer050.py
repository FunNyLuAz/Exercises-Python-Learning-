s = 0
ct = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    if n % 2 == 0:
        s += n
        ct += 1

if ct == 0:
    print('Você não informou nenhum valor par')
elif ct == 1:
    print('Você informou apenas um único valor par,', s)
else:
    print('A soma desses {} valores pares é {}'.format(ct, s))
