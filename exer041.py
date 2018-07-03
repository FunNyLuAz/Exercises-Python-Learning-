from datetime import date
an = int(input('Digite o ano de nascimento: '))
aa = date.today().year
i = aa-an

if i <= 9:
    print('Este atleta que nasceu no ano {} e tem {} de idade,'
          ' pertence a categoria MIRIM'.format(an, i))
elif 9 < i <= 14:
    print('Este atleta que nasceu no ano {} e tem {} de idade,'
          ' pertence a categoria INFANTIL'.format(an, i))
elif 14 < i <= 19:
    print('Este atleta, que nasceu no ano {} e tem {} de idade,'
          ' pertence a categoria JUNIOR'.format(an, i))
elif i == 20:
    print('Este atleta, que nasceu no ano {} e tem {} de idade,'
          ' pertence a categoria SÊNIOR'.format(an, i))
elif i > 20:
    print('Este atleta, que nasceu no ano {} e tem {} de idade,'
          ' pertence a categoria MASTER'.format(an, i))
