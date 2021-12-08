from random import randint


def sorteio(a):
    for c in range(a):
        lista.append(randint(1, 10))


def somaPar(soma):
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(soma)


lista = list()
sorteio(5)
somaPar(0)
print(lista)
