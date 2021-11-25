lista = list()
while True:
    num = int(input('Digite um número: '))
    if num not in lista:
        lista.append(num)
    conti = str(input('Quer continuar? [S/N]: ')).lower().strip()
    if conti == 'n':
        break
print(sorted(lista))