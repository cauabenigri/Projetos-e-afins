import random
import time
c = 0
while True:
    poi = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
    num = int(input(f'1... 2... 3... Digite seu número (1 á 10):'))
    if num > 10 or num < 0:
        num = int(input(f'1... 2... 3... Digite seu número (1 á 10!!!):'))
    res = random.randint(1, 10) + num
    print(f'O computador colocou {res - num}', end=', ')
    if res % 2 == 0 and poi == 'P' or res % 2 != 0 and poi == 'I':
        print('você ganhou!!')
        c += 1
    else:
        print('você perdeu!!')
        break
print(f'Você ganhou {c} vezes!!!')


