s = []
for c in range(0, 5):
    p = float(input('Digite o peso: '))
    s += [p]
print('''
O maior peso é {:.2f} Kg
O menor peso é {:.2f} Kg'''.format(max(s), min(s)))
