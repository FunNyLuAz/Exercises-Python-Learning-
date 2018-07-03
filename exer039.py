from datetime import date
an = int(input('Digite seu ano de nascimento: '))
aa = date.today().year
i = aa-an

if i > 18:
    di = i-18
    ai = aa-di
    print('O seu alistamento já passou {} anos ({})'.format(di, ai))
elif i < 18:
    di = 18-i
    ai = aa+di
    print('O seu alistamento será daqui {} anos, em {}'.format(di, ai))
else:
    print('O seu alistamento será neste ano de {}'.format(aa))
