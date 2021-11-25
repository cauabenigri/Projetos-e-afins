n = float(input('\033[1;33m digite um número: \033[m'))
print('\033[1;33m o triplo desse número é: {}{:.2f}{}'.format('\033[1;34m', n * 2, '\033[m'))
print('\033[1;33m o dobro desse número é: {}{:.2f}{}'.format('\033[1;34m', n * 3, '\033[m'))
print('\033[1;33m a raíz quadrada desse número é:  {}{:.2f}{}'.format('\033[1;34m', n ** (1/2), '\033[m'))