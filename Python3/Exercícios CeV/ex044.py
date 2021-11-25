p = float(input('Qual o preço do produto? : '))
m = int(input('''Qual o método de pagamento? : 
[ 1 ] para Dinheiro/Cheque
[ 2 ] para à vista no Cartão
[ 3 ] para 2x no Cartão
[ 4 ] para 3x ou mais no Cartão
\033[;31m>>>\033[m   '''))
if m == 1:
    print('O valor final fica R${:.2f}'.format(p - p / 100 * 10))
elif m == 2:
    print('O valor final fica R${:.2f}'.format(p - p / 100 * 5))
elif m == 3:
    print('Você vai pagar duas prestações de R${:.2f}, '.format(p / 2), end='')
    print('e o valor continuará o mesmo, R${:.2f}'.format(p))
elif m == 4:
    i = int(input('quantas parcelas? : '))
    if i >= 3:
        print('o valor final fica R${:.2f}, e você pagará em {} parcelas de R${:.2f}'.format(p + p / 100 * 20, i, p / i))
    if i == 2:
        print('você deveria ter escolhido a opção [ 3 ]')
    elif i == 1:
        print('você deveria ter escolhido a opção [ 2 ]')
else:
    print('\033[1;31mopção invalida de pagamento!!!')
