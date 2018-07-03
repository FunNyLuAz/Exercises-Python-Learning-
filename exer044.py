cl = {'zn': '\033[1;34m',
      'vn': '\033[1;32m',
      'mn': '\033[1;31m'}
p = float(input('{}Digite o valor do produto: '.format(cl['vn'])))
c = int(input('{0}{2}\n'
          '1 = Dinheiro/Cheque\n'
          '2 = À vista no cartão\n'
          '3 = 2x no cartão\n'
          '4 = 3x ou mais no cartão\n'
          '{0}{2}\n'
          '{1}Digite a condição de pagamento: '.format(cl['mn'], cl['vn'], '-=-'*20)))

if c in [1, 2, 3, 4]:
    if c == 1 or c == 2:
        if c == 1:
            pd = p-(p*0.10)
            d = 10
        elif c == 2:
            pd = p-(p*0.05)
            d = 5
        print('{}O cliente deverá pagar: {:.2f} reais, com o desconto de {}%'
              .format(cl['zn'], pd, d))
    elif c == 3 or c == 4:
        if c == 3:
            pd = p
            pc = 2
            ppc = p/2
        elif c == 4:
            pc = int(input('Digite em quantas parcelas você quer pagar: '))
            pd = p+(p*0.20)
            ppc = pd / pc
        print('{}O cliente deverá pagar: {:.2f} reais, em {}x parcelas de {:.2f} reais'
              .format(cl['zn'], pd, pc, ppc))
else:
    print('{}Valor da condição de pagamento inválido'.format(cl['zn']))
