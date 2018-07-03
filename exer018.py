import math
an = float(input('Digite o ângulo: '))
anr = math.radians(an)
s = math.sin(anr)
c = math.cos(anr)
t = math.tan(anr)
print('Seno:{:.2f}\nCosseno:{:.2f}\nTangente:{:.2f}'.format(s, c, t))
