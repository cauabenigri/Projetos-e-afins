n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
o = 1
while o != 5:
    o = int(input('Qual seria a operação?\n[1]Soma\n[2]Multiplicar\n[3]Maior\n[4]Novos Números\n[5]Sair\n   >>>'))
    if o == 1:
        print('A soma entre {} e {} é {}'.format(n1, n2, n1 + n2))
    elif o == 2:
        print('{} multiplicado por {} é {}'.format(n1, n2, n1 * n2))
    elif o == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1, n2))
        else:
            print('{} é maior que {}'.format(n2, n1))
    elif o == 4:
        n1 = int(input('Digite o novo número: '))
        n2 = int(input('Digite o outro novo número: '))
    c = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if c == 'N':
        o = 5
