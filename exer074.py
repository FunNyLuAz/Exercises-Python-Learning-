from random import randint

n1 = randint(0, 10)
n2 = randint(0, 10)
n3 = randint(0, 10)
n4 = randint(0, 10)
n5 = randint(0, 10)

nr = (n1, n2, n3, n4, n5)

print(f'''Os números sorteados são:''')
for c in range(0, 5):
    if c == 4:
        print(nr[c])
    else:
        print(nr[c], end=' - ')
print(f'''> Maior número: {max(nr)}
> Menor número: {min(nr)}''')
