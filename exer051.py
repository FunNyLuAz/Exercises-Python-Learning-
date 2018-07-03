n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

print('Os dez primeiros termos dessa PA são:')
for c in range(n, n+(r*10), r):
    if c == n+(r*9):
        print(c)
    else:
        print(c, end=', ')
