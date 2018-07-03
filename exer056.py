Ti = 0
mvn = ''
mvi = 0
m20 = 0

for c in range(1, 5):
    print('> Dados da {}°Pessoa'.format(c))
    n = input(' - Digite o nome: ').capitalize().strip()
    i = int(input(' - Digite a idade: '))
    s = input(' - Digite o sexo (M = Masc. e F = Fem.): ').upper().strip()

    Ti += i
    if s == 'M':
        if c == 1:
            mvn = n
            mvi = i
        elif mvi < i:
            mvn = n
            mvi = i
    if (s == 'F') and (i <= 20):
        m20 += 1

print('\n{}{}'.format('\033[1;32m', '-=-'*18))
#Média de Idade
mi = Ti/4
print('A média de idade dentro desse grupo é de: {:.0f} anos'.format(mi))

#Homem mais velho (Nome e Idade)
print('O homem mais velho se chama {} e tem {} anos'.format(mvn, mvi))

#Quantidade de mulheres com mais de 20 anos
print('Nesse grupo temos {} mulheres com menos de 20 anos'.format(m20))

print('{}'.format('-=-'*18))
