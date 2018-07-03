n1 = int(input('Digite um valor: '))
n2 = int(input('Digite um valor: '))
n3 = int(input('Digite um valor: '))
n4 = int(input('Digite um valor: '))

nd = (n1, n2, n3, n4)
np = 0

print(f'Números digitados: ')
for c in nd:
    print(c, end=' ')
print(f'\nO número 9 apareceu {nd.count(9)} vez(es)')
if (3 in nd) is True:
    print(f'O número 3 apareceu na {nd.index(3)+1}° Posição')
else:
    print('O número 3 não apareceu nestes números digitados')
print('O(s) número(s) par(es) digitedo(s) é(são): ', end='')
for p, c in enumerate(nd):
    if c % 2 == 0:
        print(nd[p], end=' ')
