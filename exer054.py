from datetime import date

s = 0
aa = date.today().year

for c in range(0, 7):
    a = int(input('Digite o ano de nascimento da {}° Pessoa: '.format(c+1)))
    if aa-a >= 18:
        s += 1
print('''Pessos que atigiram a maioridade: {}
Pessoas que não atingiram a maioridade: {}'''.format(s, 7-s))
