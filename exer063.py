n = int(input('Digite um valor: '))
n1 = 0
n2 = 1
c = 0

print('Os {} primeiros valores da Sequência de Fibonacci são:'.format(n))
while not c == n/2:
    if c == n/2-1:
        print('{}, {}'.format(n1, n2))
    else:
        print('{}, {},'.format(n1, n2), end=' ')
    n1 += n2
    n2 += n1
    c += 1

#Outra Maneira
'''n = int(input('Digite um valor: '))
n1 = 0
n2 = 1
c = 1

while c <= n:
    n3 = n1+n2
    print('{} -> '.format(n1, n2), end='')
    n1 = n2
    n2 = n3
    c += 1
print('FIM')'''
