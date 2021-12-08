def moeda(num='', tipo='R$'):
    return f'{tipo}{num}'


def dobro(num, boolean=False):
    num += num
    if boolean:
        return moeda(num)
    else:
        return num


def metade(num, boolean=False):
    num -= num / 2
    if boolean:
        return moeda(num)
    else:
        return num


def aumento(num, porcento, boolean=False):
    num += num / 100 * porcento
    if boolean:
        return moeda(num)
    else:
        return num


def diminui(num, porcento, boolean=False):
    num -= num / 100 * porcento
    if boolean:
        return moeda(num)
    else:
        return num


def resumo(num, aum, dim):
    print('_' * 50)
    print()
    print(' ' * 15, 'Resumo do valor')
    print('_' * 50)
    print(f'{"Preço avaliado:": <10}', f'{moeda(): >16}{num}')
    print(f'{"Dobro do Preço:": <10}', f'{moeda(): >16}{dobro(num):2f}')
    print(f'{"Metade do preço:": <10}', f'{moeda(): >15}{metade(num):.2f}')
    print(f'{f"Preço com aumento de {aum}%:": <10}', f'{moeda(): >7}{aumento(num, aum):.2f}')
    print(f'{f"Preço com diminuição de {dim}%:": <10}', f'{moeda(): >4}{diminui(num, dim):.2f}')
    print('_' * 50)
