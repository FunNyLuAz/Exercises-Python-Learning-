lp = ('Lápis', 1.75, 'Borracha', 2, 'Caderno', 15.90, 'Estojo', 25, 'Transferidor',
      4.2, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.9)

print('{:=^50}'.format(' < Lista de Produtos > '))

for ct, c in enumerate(lp):
    if ct % 2 == 0:
        print('> {:.<38}'.format(c), end='')
    else:
        print('R$:{:>7.2f}'.format(lp[ct]))

print('='*50)
