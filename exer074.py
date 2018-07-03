from random import randint

nr = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))

print(f'''Os números sorteados são:''')
for c in range(0, 5):
    if c == 4:
        print(nr[c])
    else:
        print(nr[c], end=' - ')
print(f'''> Maior número: {max(nr)}
> Menor número: {min(nr)}''')
