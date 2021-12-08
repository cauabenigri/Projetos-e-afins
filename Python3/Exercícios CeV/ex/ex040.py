import time
print('Então você quer saber sua média...')
time.sleep(2)
n1 = float(input('Sua primeira nota : '))
n2 = float(input('Sua segunda nota : '))
m = (n1 + n2) / 2
print(m)
if n1 > 10:
    print('Suas notas devem ser entre 1 e 10!!!!')
elif n2 > 10:
    print('Suas notas devem ser entre 1 e 10!!!!')
elif (n1 + n2) / 2 < 5.0:
    print('sua média ficou \033[1;31m{}\033[m, você foi  REPROVADO!!!!!!!!!!!!!!!!'.format(m))
elif m > 5.0 and m <= 6.9:
    print('sua média ficou \033[1;31m{}\033[m, você está em recuperação!!'.format(m))
elif m > 6.9:
    print('sua média ficou \033[1;32m{}\033[m, você passou'.format(m))