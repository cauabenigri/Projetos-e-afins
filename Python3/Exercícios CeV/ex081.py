lista = list()
while True:
    num = int(input('Digite um valor: '))
    lista.append(num)
    conti = str(input('Quer continuar? [S/N]: ')).upper().strip()
    if conti == 'N':
        break
con = lista[:]
con.sort(reverse=True)
print('A lista decrescente: ')
for c in con:
    print(c)
print(f'Há {len(lista)} números na lista')
if 5 in lista:
    print(f'O número 5 está na lista')
else:
    print('Não tem 5 na lista')