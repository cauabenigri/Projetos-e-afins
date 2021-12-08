list = 'Pão', 2, 'Coca-cola', 7.50, 'Coxinha', 1, 'Sonho', 2, 'Pastel', 5.50
for c in range(0, len(list)):
    if c % 2 == 0:
        print(f'{list[c]:.<20}R$', end='')
    elif c % 2 != 0:
        print(f'{list[c]: >7.2f}')