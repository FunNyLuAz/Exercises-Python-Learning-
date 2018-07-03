a = int(input('Digite um ano: '))

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ano de {} é bissexto'.format(a))
else:
    print('O ano de {} não é bissexto'.format(a))

#if a % 4 == 0:
#    bns = a
#    if bns % 100 != 0:
#        print('O ano de {} é bissexto'.format(a))
#    if bns % 100 == 0:
#        if bns % 400 == 0:
#            print('O ano de {} é bissexto'.format(a))
#        else:
#            print('O ano de {} não é bissexto'.format(a))
#else:
#    print('O ano de {} não é bissexto'.format(a))
