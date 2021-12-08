from utilidadesCeV import moeda


def erro(nume):
    global var
    if ',' in nume:
        var.append(nume.replace(',', '.'))
        print(var)
    else:
        var.append(nume)
    for c in range(0, len(var)):
        if not var[c].replace('.', '').isnumeric:
            print(var[c].replace('.', ''))
            if not nume.isnumeric():
                del var[c]
                var.insert(c, str(input('Erro: Digite o preço: ')))
                print(var)


var = list()
num = str(input('Digite o preço: '))
dim = str(input('Deseja diminuir quantos %: '))
aum = str(input('Deseja aumentar quantos %: '))
while not num.isnumeric() or not dim.isnumeric() or not aum.isnumeric():
    erro(num)
    erro(aum)
    erro(dim)
    moeda.resumo(float(var[0]), float(var[1]), float(var[2]))
    quit()
moeda.resumo(int(num), int(aum), int(dim))
