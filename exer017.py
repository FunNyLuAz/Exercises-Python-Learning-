import math
c1 = float(input('Digite o valor do cateto 1: '))
c2 = float(input('Digite o valor do cateto 2: '))

#h = math.hypot(c1, c2)
h = math.sqrt((pow(c1, 2))+(pow(c2, 2)))

print('Hipotenusa:', h)
