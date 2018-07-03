a = float(input('Digite sua altura: '))
p = float(input('Digite seu peso: '))

imc = p/(a**2)

print('Seu IMC é de {:.1f}'.format(imc))

if imc < 18.5:
    print('Você está abaixo do peso ideal')
elif 18.5 <= imc < 25:
    print('Você está dentro do peso ideal')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('Você está com obesidade')
elif 40 <= imc:
    print('Você está com obesidade mórbida')
