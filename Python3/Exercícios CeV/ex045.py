from time import sleep
from random import randint
print('=' * 159)
print('                                                                Pedra, Papel, Tesoura')
print('=' * 159)
sleep(2)
pedra = 1
papel = 2
t = 3
n = randint(1, 3)
p = int(input('''Pedra, papel ou tesoura? : 
[ 1 ] para Pedra
[ 2 ] para Papel
[ 3 ] para Tesoura
\033[;31m>>>\033[m   '''))
if p != 1 and p != 2 and p != 3:
    print('\033[1;31mOpção invalida\033[m')
sleep(1)
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura...')
print('-' * 29)
if n == 3 and p == 2:
    print('Coloquei Tesoura, você perdeu')
elif n == 2 and p == 1:
    print(' Coloquei Papel, você perdeu ')
elif n == 1 and p == 3:
    print(' Coloquei Pedra, você perdeu ')
elif n == 2 and p == 3:
    print(' Coloquei Papel, você ganhou ')
elif n == 1 and p == 2:
    print(' Coloquei Pedra, você ganhou ')
elif n == 3 and p == 1:
    print('Coloquei Tesoura, você ganhou')
elif n == p:
    print('Eu e você colocamos o mesmo!!')
print('-' * 29)