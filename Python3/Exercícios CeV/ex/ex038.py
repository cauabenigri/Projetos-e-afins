import time
print('Supomos que você queira saber qual número é maior q o outro')
time.sleep(2)
n1 = float(input('Digite o primeiro número : '))
n2 = float(input('Digite o segundo número : '))
if n1 > n2:
    print('\033[1;33m{:.2f}\033[m é maior que \033[1;33m{:.2f}\033[m!'.format(n1, n2))
elif n2 > n1:
    print('\033[1;33m{:.2f}\033[m é maior que \033[1;33m{:.2f}\033[m!'.format(n2, n1))
else:
    print('Não tem maior, os dois são iguais')