from time import sleep
n = int(input('> Digite o primeiro termo da PA: '))
r = int(input('> Digite a razão da PA: '))
c = n
cd = 10
cf = 0
ct = 0

print('\nOs dez primeiros termos dessa PA são:')

while cd is not False:
    while not ct == cd:
        if ct == cd-1:
            print(c)
        else:
            print(c, end=', ')
        c += r
        ct += 1
    cf = int(input('\n> Gostaria de ver mais quantos termos? '))
    cd += cf
    if cf == 0:
        cd = False
        print('Encerrando...')
        sleep(0.7)
        print('Foram mostrados {} termos desta PA'.format(ct))
