a = c = maior = menor = 0
b = 1
while b != 0:
    b += 1
    d = int(input('Digite um número para fazermos uma média ou digite 0 para terminar de digitar: '))
    a = a + d
    if d != 0:
        c = c + 1
    if b == 2:
        menor = maior = d
    if d > maior:
        maior = d
    elif d < menor and d != 0:
        menor = d
    if d == 0:
        print('A média aritmética destes números é {}\nO maior numero foi {}\nO menor número foi {}'.format(a / c, maior, menor))
        e = str(input('Deseja continuar [S/N]: ')).strip().upper()[0]
        if e == 'N':
            b = 0
