e = ' '.join(input('Digite a expressão: ')).split()
v = ['', ' não']
vd = 0

#Outra Maneira:
'''vd = []

for c in e:
    if c == '(':
        vd.append(c)
    elif c == ')':
        if len(vd) > 0:
            vd.pop()
        else:
            vd.append(')')
            break
print(vd)
print(f'Sua expressão{v[0] if len(vd) == 0 else v[1]} é válida')'''

for c in e:
    if c == '(':
        vd += 1
    elif c == ')':
        vd -= 1
    print(vd)
print(f'Sua expressão{v[0] if vd == 0 else v[1]} é válida')
