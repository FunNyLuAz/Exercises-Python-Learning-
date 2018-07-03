cl = {'cr': '\033[m',
      'zn': '\033[1;34m',
      'rn': '\033[1;35m',
      'an': '\033[1;33m',
      'vn': '\033[1;32m',
      'mn': '\033[1;31m'}
n = int(input('{}Digite um número: '.format(cl['vn'])))

c = int(input('{3}{4}\n'
          '{0}1 = Binário\n'
          '{1}2 = Octal\n'
          '{2}3 = Hexadecimal\n'
          '{3}{4}\n'
          '{5}Digite o valor que indica a conversão que você deseja: '
          .format(cl['zn'], cl['rn'], cl['an'], cl['vn'], '-=-'*20, cl['mn'])))

if c == 1:
    nc = bin(n)[2:]
    print('{}O número {} convertido para binário fica {:8}'.format(cl['zn'], n, nc,))
elif c == 2:
    nc = oct(n)[2:]
    print('{}O número {} convertido para octal fica {}'.format(cl['rn'], n, nc))
elif c == 3:
    nc = hex(n)[2:]
    print('{}O número {} convertido para hexadecimal fica {}'.format(cl['an'], n, nc))
else:
    print(cl['vn'], 'O número digitado é inválido')
