cl = {'zn': '\033[1;34m',
      'an': '\033[1;33m'}

n = int(input('Digite um número: '))

print('{}{}'.format(cl['zn'], '-=-'*4))
for c in range(1, 11):
    print('{}{} x {:2} = {}'.format(cl['an'], n, c, (n * c)))
print('{}{}'.format(cl['zn'], '-=-'*4))
