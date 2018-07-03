n = s = c = 0

while not n == 999:
    n = int(input('> Digite um valor [999 = Stop]: '))
    if n != 999:
        s += n
        c += 1

print('A soma desses {} valores é de {}'.format(c, s))

#Outra Maneira
'''n = s = c = 0

n = int(input('> Digite um valor [999 = Stop]: '))
while not n == 999:
    s += n
    c += 1
    n = int(input('> Digite um valor [999 = Stop]: '))

print('A soma desses {} valores é de {}'.format(c, s))'''
