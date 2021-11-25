lista = []
for c in range(0, 5):
    num = int(input('Digite um valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
    elif num < lista[0]:
        lista.insert(0, num)
    for d in range(len(lista)):
         if lista[d - 1] < num < lista[d]:
             lista.insert(d, num)
print(lista)
