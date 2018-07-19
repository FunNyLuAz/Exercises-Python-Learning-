gp = []
p = []
pe = []
ma = me = c = 0
man = men = ''

while True:
    c += 1
    print(f'{f"< Dados da {c}ª Pessoa >":-^40}')
    p.append(input(f' > Digite o nome: '))
    p.append(float(input(f' > Digite o peso: ')))
    gp.append(p[:])
    pe.append(p[1])
    p.clear()
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    print('')
    if r == 'N':
        break

for c in gp:
    if c[1] == max(pe):
        ma = c[1]
        man += c[0]
    elif c[1] == min(pe):
        me = c[1]
        men += c[0]

print(f''' > Dados cadastrados:
 -Quantidade de pessoas cadastradas: {len(gp)}
 -Pessoa(s) mais pesada(s): {man} (Com {ma:.1f}Kg)
 -Pessoa(s) menos pesada(s): {men} (Com {me:.1f}Kg)''')
