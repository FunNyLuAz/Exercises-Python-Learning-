n = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = n
ct = 0

print('Os dez primeiros termos dessa PA são:')

while not ct == 10:
    if ct == 9:
        print(c)
    else:
        print(c, end=', ')
    c += r
    ct += 1
