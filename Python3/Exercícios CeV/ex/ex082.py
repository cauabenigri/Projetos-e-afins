lista = list()
listai = list()
listap = list()
while True:
    lista.append(int(input('Digite um valor: ')))
    conti = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if conti == 'N':
        break
print('todos os números: ')
for c in lista:
    print(c)
print('todos os números pares: ')
for d in lista:
    if d % 2 == 0:
        print(d)
print('Todos os números impares: ')
for e in lista:
    if e % 2 != 0:
        print(e)
