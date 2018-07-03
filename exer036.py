c = float(input('Digite o valor da casa: '))
s = float(input('Digite seu salário: '))
a = int(input('Digite em quantos anos você quer pagar: '))

vp = c/(a*12)

if vp > s*0.30:
    print('Este empréstimo foi negado\n'
          'O valor da mensalidade ({:.2f} reais) ultrapassa 30% de seu salário'.format(vp))
else:
    print('Este empréstimo foi aprovado'
          '\nO valor da mensalidade ({:.2f} reais) não ultrapassa 30% de seu salário'.format(vp))
