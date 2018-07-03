from time import sleep
np = 1
m18 = h = m20 = 0
s = r = ' '

while True:
    print(f'Dados da {np}°Pessoa'if np == 1 else f'\nDados da {np}°Pessoa')
    i = int(input('Digite sua idade: '))
    s = ' '
    while s not in 'MF':
        s = input('Digite seu sexo [M/F]: ').strip().upper()[0]
    r = ' '
    while r not in 'SN':
        r = input('Cadastrar mais uma pessoa? [S/N]: ').strip().upper()[0]
    np += 1
    if i >= 18:
        m18 += 1
    if s in 'M':
        h += 1
    if (s in 'F') and (i < 20):
        m20 += 1
    if r in 'S':
        print('\n -Preparando para cadastrar mais uma pessoa...')
        sleep(0.7)
    elif r in 'N':
        break

print(f'''\n> Foram cadastrados:
-{m18} pessoa(s) com mais de 18 anos
-{h} homem(ns)
-{m20} mulher(es) com menos de 20 anos''')
