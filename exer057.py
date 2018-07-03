s = ' '
ss = ''

while s not in 'MF':
    s = input('Digite seu sexo [M/F]: ').upper().strip()[0]
    if s not in 'MF':
        print('\033[1;31m> Digite um valor válido\033[m\n')

if s == 'M':
    ss = '\033[1;4;34mMASCULINO'
elif s == 'F':
    ss = '\033[1;4;31mFEMININO'

print('\n{0}{1}\n> O seu sexo é {2}\n{0}{1}'.format('\033[1;32m', '-=-'*8, ss))

#Outra maneira:
#s = input('Digite seu sexo [M/F]: ').strip().upper()[0]
#while s not in 'MF':
#    s = input('Dados inválidos, porfavor digite seu sexo [M/F]: ')
#print('Sexo {} registrado com sucesso'.format(s))
