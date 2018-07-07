e = ' '.join(input('Digite a expressão: ')).split()
c = op = ed = 0
v = ['', ' não']

while True:
    if c == len(e):
        break
    if e[c] is '(':
        op += 1
    if e[c] is ')':
        ed += 1
    c += 1

print(f'Sua expressão{v[0] if op == ed else v[1]} é válida')
