c = input('Digite o nome da sua cidade: ')
cc = c.upper().split()
cv = 'SANTO' in cc[0]

print('O nome da sua cidade apresenta Santo no começo?', cv)
#print('O nome da sua cidade apresenta Santo no começo?', cc[0].upper() == 'SANTO')
#print('O nome da sua cidade apresenta Santo no começo?', c[:5].upper() == 'SANTO')
