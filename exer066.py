s = c = 0

while True:
    n = int(input('Digite um valor [999 = Stop]: '))
    if n == 999:
        break
    s += n
    c += 1

print(f'''\nValores digitados: {c}
Soma total resultante: {s}''')
