m = 0
c = 0
r = ' '
li = []

while r not in 'N':
    n = int(input('> Digite um valor: '))
    r = input('Quer continuar a digitar? [S/N]: ').upper().strip()[0]
    m += n
    c += 1
    li += [n]

print('''\nDesses {} valores digitados temos as seguintes informações:
A média dos valores digitados é de: {:.1f}
O maior valor é: {}
O menor valor é: {}'''.format(c, m/c, max(li), min(li)))
