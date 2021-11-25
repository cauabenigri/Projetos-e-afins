matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = 0
soma3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]'))
        if c == 2:
            soma3 += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[ {matriz[l][c]: ^5} ]', end='')
    print()
print(f'A soma de todos os valores pares é {soma}')
print(f'A soma dos valores da 3ª linha é {soma3}')
print(f'O maior valor da 2ª linha é {max(matriz[1])}')
