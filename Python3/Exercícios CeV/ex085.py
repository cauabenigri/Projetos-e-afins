lista = [[], []]
for i in range(1, 8):
    num = int(input('Digite um valor: '))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[1].sort()
lista[0].sort()
print(f'Os números ímpares são {lista[1]}, e os números pares são {lista[0]}')
