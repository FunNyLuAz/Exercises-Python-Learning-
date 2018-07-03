d = int(input('Digite o número de dias do carro alugado: '))
km = float(input('Digite o número de KMs rodados pelo carro alugado: '))
pd = 60*d
pkm = 0.15*km
p = pd+pkm
print('Você terá que pagar: R${:.2f}'.format(p))
