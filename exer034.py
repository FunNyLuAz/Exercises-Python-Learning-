s = float(input('Digite o valor do salário: '))
if s > 1250:
    print('Com o aumento, o salário ficaria como: {:.2f} reais'.format(s*1.10))
else:
    print('Com o aumento, o salário ficaria como: {:.2f} reais'.format(s*1.15))
