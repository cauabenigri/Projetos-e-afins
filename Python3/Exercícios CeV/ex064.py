a = 0
cont = 0
soma = 0
while a != 999:
    a = int(input('Digite um número: '))
    cont = cont + 1
    if a != 999: soma = soma + a
print('{} números foram digitados até chegar no número "999", e a soma destes números é {}'.format(cont, soma))
