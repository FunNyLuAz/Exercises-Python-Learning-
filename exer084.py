gp = []
p = []
ma = me = c = 0
man = men = ''

while True:
    c += 1
    print(f'{f"< Dados da {c}ª Pessoa >":-^40}')
    p.append(input(f' > Digite o nome: '))
    p.append(float(input(f' > Digite o peso: ')))

    if len(gp) == 0:
        ma = me = p[1]
    elif p[1] >= ma:
        ma = p[1]
    elif p[1] <= me:
        me = p[1]

    gp.append(p[:])
    p.clear()
    r = ' '
    while r not in 'SN':
        r = input('Quer continuar? [S/N]: ').strip().upper()[0]
    print('')
    if r == 'N':
        break

for c in gp:
    if c[1] == ma:
        man += c[0]+', '
    elif c[1] == me:
        men += c[0]+', '

print(f''' > Dados cadastrados:
 -Quantidade de pessoas cadastradas: {len(gp)}
 -Pessoa(s) mais pesada(s): {man[:-2]} (Com {ma:.1f}Kg)
 -Pessoa(s) menos pesada(s): {men[:-2]} (Com {me:.1f}Kg)''')
