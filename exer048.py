s = 0
ct = 0
for c in range(0, 501, 3):
    if c % 2 != 0:
        s += c
        ct += 1
print('A soma entre todos os números ímpares multiplos de 3 entre 0 e 500 ({} números) é {}'
      .format(ct, s))

#s = 0
#ct = 0
#for c in range(1, 501, 2):
#    if c % 3 == 0:
#        s += c (ou s = s+c)
#        ct += 1 (ou ct = ct+1)
#print('A soma entre todos os números ímpares multiplos de 3 entre 0 e 500 ({} números) é {}'
#      .format(ct, s))
