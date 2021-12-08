maior = 0
menor = 0
for c in range(1, 6):
    p = float(input('Qual o peso da {}ª pessoa : '.format(c)))
    if c == 1:
        maior = p
        menor = p
    if p > maior:
        maior = p
    if p < menor:
        menor = p
print('O maior peso foi {:.2f} e o menor peso foi {:.2f}'.format(maior, menor))