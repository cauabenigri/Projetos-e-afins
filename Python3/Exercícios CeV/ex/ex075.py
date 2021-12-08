a = int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: ')), int(input('Digite um número: '))
print(f'O valor 9 apareceu {a.count(9)} vezes,')
cont = 0
if 3 in a:
    print(f'o número 3 apareceu na posição {a.index(3) + 1}')
else:
    print(f'o valor 3 não esta em {a}')
for c in a:
    if c % 2 == 0:
        cont += 1
print(f'e {cont} números são pares')