n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda note: '))

m = (n1+n2)/2

if (n1 and n2 <= 10.0) and (n1 and n2 >= 0):
    if 7.0 <= m <= 10.0:
        print('Este aluno passou com {:.1f} na média'.format(m))
    elif 7.0 > m >= 5.0:
        print('Este aluno ficou para recuperação, com {:.1f} na média'.format(m))
    elif m < 5.0:
        print('Este aluno reprovou com {:.1f} na média'.format(m))
else:
    print('A média {:.1f}, dada pelas notas {} e {}, não é válida, '
          'digite notas entre 0 e 10'.format(m, n1, n2))
