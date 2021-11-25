total = qt = barato = nmbarato = c = 0
while True:
    nome = str(input('Qual é o nome do produto?: '))
    pre = float(input('Qual é o preço do produto?: '))
    total += pre
    if pre > 1000:
        qt += 1
    if c == 0:
        nmbarato = nome
        c += 1
        barato += pre
    elif pre < barato:
        nmbarato = nome
    con = str(input('Deseja continuar? [S/N]: ')).strip().upper()
    if con == 'N':
        break
print(f'No total serão gastos R${total}, {qt} produtos custam mais de R$1000,00 e o produto mais barato é {nmbarato}, custando R${barato}')
