from ex108 import moeda


def dobro(num, bool=False):
    num += num
    if bool:
        return moeda(num)
    else:
        return num


def metade(num, bool=False):
    num -= num / 2
    if bool:
        return moeda(num)
    else:
        return num


def aumento(num, porcento, bool=False):
    num += num / 100 * porcento
    if bool:
        return moeda(num)
    else:
        return num


def diminui(num, porcento, bool=False):
    num -= num / 100 * porcento
    if bool:
        return moeda(num)
    else:
        return num
