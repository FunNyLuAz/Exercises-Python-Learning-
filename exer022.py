n = input('Digite seu nome completo: ')

print('Caso seu nome tivesse apenas letras maiúsculas ficaria:', n.upper())

print('Caso seu nome tivesse apenas letras mainúsculas ficaria:', n.lower())

print('Seu nome tem no total {} de letras'.format(len(n.replace(' ', ''))))
#print('Seu nome tem no total {} de letras'.format(len(n) - n.count(' ')))

print('Seu primeiro nome tem no total {} de letras'.format(len(n.split()[0])))
#print('Seu primeiro nome tem no total {} de letras'.format(n.find(' ')))
