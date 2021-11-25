from datetime import date
a = date.today().year
n = int(input('Em que ano você nasceu? : '))
i = a - n
if n >= a:
    print('seu engraçadinho')
elif n <= 1900:
    print('seu engraçadinho')
elif i <= 9:
    print('Mirim')
elif i > 9 and i <= 14:
    print('Infantil')
elif i > 14 and i <= 19:
    print('Júnior')
elif i > 19 and i <= 25:
    print('Sênior')
else:
    print('Master')
