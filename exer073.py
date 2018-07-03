cl = {'cr': '\033[m',
      'zn': '\033[1;34m',
      'rn': '\033[1;35m',
      'an': '\033[1;33m',
      'vn': '\033[1;32m',
      'mn': '\033[1;31m'}

cb2018 = ('Flamengo', 'Atlético', 'São Paulo', 'Internacional', 'Grêmio',
          'Palmeiras', 'Sport Recife', 'Cruzeiro', 'Botafogo', 'Corinthians',
          'Vasco da Gama', 'Fluminense', 'América-MG', 'Chapecoense', 'Santos',
          'EC Vitória', 'Bahia', 'Paraná', 'Atlético-PR', 'Ceará SC')

print(f'''{cl['zn']}{'-=-'*20}
{cl['vn']} > Lista dos colocados do Brasileirão 2018:
{cb2018}

 > 5 Primeiros colocados:
{cb2018[:5]}

 > 4 Últimos colocados:
{cb2018[-4:]}

 > Em ordem alfabética:
{sorted(cb2018)}

 > Posição do Chapecoense:
{cb2018.index('Chapecoense')+1}° Posição
{cl['zn']}{'-=-'*20}''')
