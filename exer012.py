pc = float(input('Digite o preço do produto: R$'))
d = (pc/100)*5
pd = pc-d
print('O preço com 5% de desconto é: R${:.2f}'.format(pd))
