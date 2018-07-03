f = input('Digite um frase: ').strip()
fu = f.upper()
fa = fu.count('A')

print('A letra A apareceu {} vezes'.format(fa))
print('A letra A apareceu pela primeira vez na posição:{}°'.format(fu.find('A')+1))
print('A letra A apareceu pela última vez na posição:{}°'.format(fu.rfind('A')+1))
