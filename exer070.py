from time import sleep
np = 1
npb = r = ' '
ppb = p1000 = pt = c = 0

while True:
    print(f'Cadastro do produto {np}')
    n = input('Informe o nome do produto: ').strip()
    p = float(input('Informe o preço do produto: R$'))
    while r not in 'SN':
        r = input(' > Cadastrar mais um produto [S/N]: ').strip().upper()[0]
    pt += p
    c += 1
    np += 1
    if p >= 1000:
        p1000 += 1
    if c == 1 or p < ppb:
        npb = n
        ppb = p
    if r in 'S:':
        print('\nPreparando para cadastrar mais um produto...\n')
        sleep(0.7)
    elif r in 'N':
        print('\nPROCESSANDO DADOS...\n')
        sleep(0.7)
        break
    r = ' '

print(f'''Total gasto: R${pt:.2f}
Produtos que custam mais de R$1000: {p1000}
Produto mais barato: {npb}, que custa R${ppb:.2f}''')
