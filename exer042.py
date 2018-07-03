r1 = float(input('Digite a reta 1: '))
r2 = float(input('Digite a reta 2: '))
r3 = float(input('Digite a reta 3: '))

rl = [r1, r2, r3]

if ((r2-r3) < r1 < r2+r3) and ((r1-r3) < r2 < r1+r3) and ((r1-r2) < r3 < r1+r2):
    if r1 == r2 == r3:
        print('A partir dessas retas é possível construir um triângulo equilátero')
    elif (r1 == (r2 or r3)) or (r2 == (r1 or r3)) or (r3 == (r1 or r2)):
        print('A partir dessas retas é possível construir um triângulo isósceles')
    elif r1 != r2 != r3:
        print('A partir dessas retas é possível construir um triângulo escaleno')
else:
    print('A partir dessas retas não é possível construir um triângulo')
