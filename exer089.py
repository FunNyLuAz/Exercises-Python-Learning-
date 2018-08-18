from time import sleep

tm = []
a = []
na = []
nn = []
nd1 = nd2 = -1
n = c = 0

while True:
    c += 1
    print(f'{f"--< {c}º Aluno >":-<25}')
    na.append(input('Digite o nome do aluno(a): ').capitalize())
    while not 0 <= nd1 <= 10:
        nd1 = float(input('Digite a 1ª Nota: '))
    while not 0 <= nd2 <= 10:
        nd2 = float(input('Digite a 2ª Nota: '))

    nn.append(nd1)
    nn.append(nd2)
    a.append(na[:])
    a.append(nn[:])
    tm.append(a[:])

    na.clear()
    nn.clear()
    a.clear()
    nd1 = nd2 = -1

    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if r == 'N':
        print('\nPROCESSANDO DADOS...')
        sleep(0.7)
        break

print(f'''\n > Tabela - Médias:
Nº  {"Nome":<16}{"Média":>7}''')
for p, c in enumerate(tm):
    print(f'{p:0>2}  {c[0][0]:.<16}{(c[1][0]+c[1][1])/2:.>7.2f}')

print('\n > Notas - Individuais:')
while n != 999:
    n = int(input('Digite o Nº do Aluno: '))
    if n != 999:
        try:
            print(f'As notas do aluno {tm[n][0][0]} são {tm[n][1][0]:.2f} e {tm[n][1][1]:.2f}\n')
        except IndexError:
            print(f'\033[4;31mAluno não encontrado, tente novamente\033[m\n')
