nn = []
n1 = n2 = -1
c = ct = 0

while c != 5:
    n = int(input(' > Digite um valor: '))
    if (n in nn) is True:
        nn.insert(nn.index(n), n)
        p = nn.index(n)+1
    elif c == 0 or (n > nn[len(nn)-1]):
        nn.append(n)
        p = len(nn)
    else:
        if n < nn[0]:
            nn.insert(0, n)
            p = 1
        elif n1 > n > n2:
            nn.insert(nn.index(n1), n)
            p = nn.index(n1)+1
        elif n2 > n > n1:
            nn.insert(nn.index(n2), n)
            p = nn.index(n2)+1
        elif n not in nn:
            while True or ct != 5:
                if n > nn[ct]:
                    nn.insert(ct+2, n)
                    p = ct+2
                    break
                elif n < nn[ct]:
                    nn. insert(ct-1, n)
                    p = ct
                    break
                ct += 1
        n2 = n1
        n1 = n
    c += 1
    print(f' -Valor adicionado à {p}ª Posição')

print('\nValores digitados: ')
for p, c in enumerate(nn):
    if p == len(nn)-1:
        print(c)
    else:
        print(c, end=' - ')
