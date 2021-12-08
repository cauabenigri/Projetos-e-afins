import ex107


def moeda(num='', tipo='R$'):
    return f'{tipo}{num}'


def resumo(num, aum, dim):
    print('_' * 50)
    print()
    print(' ' * 15, 'Resumo do valor')
    print('_' * 50)
    print(f'{"Preço avaliado:": <10}', f'{moeda(): >16}{num}')
    print(f'{"Dobro do Preço:": <10}', f'{moeda(): >16}{ex107.dobro(num)}')
    print(f'{"Metade do preço:": <10}', f'{moeda(): >15}{ex107.metade(num)}')
    print(f'{f"Preço com aumento de {aum}%:": <10}', f'{moeda(): >7}{ex107.aumento(num, aum)}')
    print(f'{f"Preço com diminuição de {aum}%:": <10}', f'{moeda(): >4}{ex107.diminui(num, dim)}')
    print('_' * 50)
