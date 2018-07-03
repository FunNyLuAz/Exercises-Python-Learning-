v = float(input('Digite a velocidade do carro: '))
if v > 80:
    print('Você foi multado, pague: {:.2f} reais'.format((v-80)*7))
else:
    print('Parabéns, continue assim')
