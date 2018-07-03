cl = {'cr': '\033[m',
      'zn': '\033[1;34m',
      'xn': '\033[1;36m',
      'an': '\033[0;33m',
      'vn': '\033[1;32m',
      'mn': '\033[1;31m'}

n = int(input('Digite um número inteiro: '))
tg = '-=-'*12

p = 0
print('''{0}{1}
{0}Números Azuis: Múltiplos de {2}
Números Vermelhos: Não Múltiplos de {2}
{0}{1}'''.format(cl['xn'], tg, n))

for c in range(1, n):
    if n % c == 0:
        print(cl['zn'], end='')
        if c != 1 and n:
            p = 1
    elif n % c != 0:
        print(cl['mn'], end='')
    print(c, end='\033[1;33m - ')
print('{}{}'.format(cl['zn'], n))

if n == (0 or 1):
    print(cl['zn'], '> O número {1}{0}{2} é uma exceção'
          .format(n, cl['an'], cl['zn']))
elif p == 0:
    print(cl['zn'], '> O número {1}{0}{2} é primo'
          .format(n, cl['an'], cl['zn']))
elif p != 0:
    print(cl['mn'], '> O número {1}{0}{2} não é primo'
          .format(n, cl['an'], cl['mn']))

#s = 0
#for c in range(2, 14):
#    if (n % c != 0) and (n != c):
#        s += c
#
#if (s == 90) or (90 == s+n):
#    print('Este número é primo')
#else:
#    print('Este número não é primo')
