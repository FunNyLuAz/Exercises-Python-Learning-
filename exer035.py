r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))

rl = [r1, r2, r3]

if ((r2-r3) < r1 < r2+r3) and ((r1-r3) < r2 < r1+r3) and ((r1-r2) < r3 < r1+r2):
    print('A partir dessas retas é possível construir um triângulo')
else:
    print('A partir dessas retas não é possível construir um triângulo')
