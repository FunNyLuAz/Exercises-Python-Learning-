n = int(input('Digite um valor: '))
#nf para os outros Meios de resolução
#nf = n-1
nf = n
nr = n

#Meios de resolução
#Usando while
#while not nf == 0:
#    nr *= nf
#    nf -= 1

#Usando for
#for c in range(n, 1, -1):
#    nr *= nf
#    nf -= 1

#Usando Math
#from math import factorial
#nr = factorial(n)

#Resposta (Compatível com todos)
#print(' > {}! = '.format(n), end='')
#for c in range(n, 0, -1):
#    if c == 1:
#        print(c, end=' = ')
#    else:
#        print(c, end=' x ')
#print(nr)

#Meio de resolução + Resposta (Usando o while)
print(' > {0}! = {0} x '.format(n), end='')
while not nf == 1:
    nf -= 1
    nr *= nf
    print(nf, 'x ' if nf > 1 else '= ', end='')
print(nr)
