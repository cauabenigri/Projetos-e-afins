n = int(input('\033[1;37mdigite um número : '))
s = n + 1
a = n - 1
print('\033[1;37mo antecessor de {}{}{} \033[1;37mé {}{}{}, \033[1;37me o sucessor é {}{}{}'.format('\033[1;33m', n, '\033[m', '\033[1;35m', a, '\033[m', '\033[1;32m', s, '\033[m'))