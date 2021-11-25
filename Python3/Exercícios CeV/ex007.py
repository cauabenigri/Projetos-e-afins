n1 = float(input('\033[1;35mQual a sua primeira nota? : '))
n2 = float(input('Qual a sua segunda nota? : '))
nota = (n1 + n2) / 2
if nota > 10:
    print('suas notas devem estar entre 1 e 10')
elif nota >= 7:
    print('Sua média é {}{:.2f}{}'.format('\033[1;32m', nota, '\033[m'))
else:
    print('Sua média é {}{:.2f}{}'.format('\033[1;31m', nota, '\033[m'))