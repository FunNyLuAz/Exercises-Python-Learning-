#Modo Matemático
n = int(input('Digite um número entre 0 e 9999: '))

m = n//1000 % 10
print('O número que aparece na casa dos milhares é:', m)

c = n//100 % 10
print('O número que aparece na casa das centenas é:', c)

d = n//10 % 10
print('O número que aparece na casa das dezenas é:', d)

u = n//1 % 10
print('O número que aparece na casa das unidades é:', u)



#Modo de Manipulação de Texto (Dá erro, caso não se insire 4 dígitos)
#n = input('Digite um número entre 0 e 9999: ')

#print('O número que aparece na casa dos milhares é:', n[0])

#print('O número que aparece na casa das centenas é:', n[1])

#print('O número que aparece na casa das dezenas é:', n[2])

#print('O número que aparece na casa das unidades é:', n[3])


#Modo Matemático - Lucas(Não dá erro)
#import math
#n = int(input('Digite um número entre 0 e 9999: '))

#m = math.trunc(n/1000)
#print('O número que aparece na casa dos milhares é:', m)

#c = math.trunc(n/100-m*10)
#print('O número que aparece na casa das centenas é:', c)

#d = math.trunc(n/10-m*100-c*10)
#print('O número que aparece na casa das dezenas é:', d)

#u = math.trunc(n-m*1000-c*100-d*10)
#print('O número que aparece na casa das unidades é:', u)
