from random import randint
n = randint(1, 10)
n1 = 1
print('_'*29, 'Advinha', '_'*29)
p = int(input('O computador pensou em um número entre 1 e 10, advinhe: '))
while n != p:
    p = int(input('Errado, tente novamente: '))
    n1 = n1 + 1
    if p > n:
        print('Menos...')
    elif p < n:
        print('Mais...')
print('Acertou! Foram necessárias {} tentativas'.format(n1))
