import time
print('Suponhamos que você queira comprar uma casa...')
time.sleep(2)
casa = float(input('Qual o valor da casa? : '))
sal = float(input('Qual o seu salário? : '))
anos = int(input('Em quantos anos quer pagar? : '))
tempo = anos * 12
valor = casa / tempo
p = casa / (12 * anos)
print('Você quer pagar os R${:.2f} da casa em {} anos, com a prestação de R${:.2f} por mês...'.format(casa, anos, p))
if p > sal / 100 * 30:
    print('de acordo com seu salário, você provavelmente não conseguirá pagar a casa...')
else:
    print('de acordo com seu salário, se você se esforçar você consegue!!!')