validacaoint = validacaofloat = False


def leiaint():
    global validacaoint, validacaofloat
    while not validacaoint:
        try:
            n = int(input('Digite um valor inteiro: '))
        except Exception as erro:
            print(f'Erro de {erro.__class__} (número não inteiro) encontrado!')
        else:
            validacaoint = True
    while not validacaofloat:
        try:
            r = float(input('Digite um valor real: '))
        except Exception as erro:
            print(f'Erro de {erro.__class__} (número não real) encontrado!')
        else:
            validacaofloat = True
    print(f'O valor inteiro foi: {n} e o valor real foi: {r}')


leiaint()
