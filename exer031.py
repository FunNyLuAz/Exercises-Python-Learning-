km = float(input('Digite a distância da sua viajem em Km: '))
if km > 200:
    print('Sua viajem lhe custará: {:.2f} reais'.format(km*0.45))
else:
    print('Sua viajem lhe custará: {:.2f} reais'.format(km*0.5))
