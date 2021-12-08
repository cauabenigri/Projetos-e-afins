def leiaint(qst):
    num = input(qst)
    while not num.isnumeric():
        print('Erro! ', end='')
        num = input(qst)
    return num


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')