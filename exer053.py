f = input('Digite uma frase: ').strip().upper()
fs = ''.join(f.split())
s = ''

for c in range(len(fs), 0, -1):
    s += fs[c-1]
#s = fs[::-1] (Jeito alternativo)

print('Invertida, a frase {} resultaria em {}'.format(fs, s))
if fs == s:
    print('Esta frase é um palindromo')
else:
    print('Esta frase não é um palindromo')
