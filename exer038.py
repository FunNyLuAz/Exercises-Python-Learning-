n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))

if n1 > n2:
    print('O primeiro valor {} é maior que o segundo {}'.format(n1, n2))
elif n2 > n1:
    print('O segundo valor {} é maior que o primeiro {}'.format(n2, n1))
elif n1 == n2:
    print('Os dois valores são iguais')
