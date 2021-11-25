c = '-=-'
print('{}{}Calculadora de Soma{}{}'.format('\033[1;31m', c * 22, c * 23, '\033[m'))
n = float(input('\033[1;35mdigite um número : \033[m'))
n1 = float(input('\033[1;35mdigite outro número : \033[m'))
print('{}a soma entre {:.2f} e {:.2f} é igual a {:.2f}{}'.format('\033[1;31m', n, n1, n + n1, '\033[m'))