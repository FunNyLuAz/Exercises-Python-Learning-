lp = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor',
      4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print(f'{" < Lista de Produtos > ":=^50}')

for ct, c in enumerate(lp):
    if ct % 2 == 0:
        print(f'> {c:.<38}', end='')
    else:
        print(f'R$:{c:>7.2f}')

print('='*50)
