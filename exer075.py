nd = (int(input(' > Digite um valor: ')), int(input(' > Digite um valor: ')),
      int(input(' > Digite um valor: ')), int(input(' > Digite um valor: ')))
np = 0

print(f'\nNúmeros digitados: \033[1;34m')
for ct, c in enumerate(nd):
    if ct != 3:
        print(c, end=' - ')
    else:
        print(c)
print(f'\n\033[m -O número 9 apareceu {nd.count(9)} vez(es)')
if 3 in nd:
    print(f' -O número 3 apareceu na {nd.index(3)+1}° Posição')
else:
    print(' -O número 3 não apareceu nestes números digitados')
print(' -O(s) número(s) par(es) digitedo(s) é(são): ', end='')
for p, c in enumerate(nd):
    if c % 2 == 0:
        print(nd[p], end=' ')
