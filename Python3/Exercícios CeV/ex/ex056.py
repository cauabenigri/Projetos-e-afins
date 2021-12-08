import datetime
ano = datetime.date.today().year
m = 0
maiorh = 0
nmh = None
mcm20a = 0
for a in range(1, 5):
    print('\033[1;31m={}ª Pessoa=\033[m'.format(a))
    n = str(input('\033[0;33mQual o nome da {}ª pessoa? : '.format(a)))
    i = int(input('Qual a idade da {}ª pessoa? : '.format(a)))
    s = int(input('Qual o sexo da {}ª pessoa?\033[m\n\033[1;33m   1 -> feminino\n   2 -> masculino\033[m\n\033[1;31m>>>\033[m   '.format(a)))
    if s != 1 and s != 2:
        print('\033[1;31mOpção inválida, tente novamente\033[m')
        quit()
    m = m + i
    if s == 2:
        if a == 1:
            maiorh = i
            nmh = n
        if i > maiorh:
            maiorh = i
            nmh = n
    if s == 1:
        if i < 20:
            mcm20a = mcm20a + 1
print('\033[1;31m=Resultados=\033[m')
print(('\033[0;32mA média de idade dessas pessoas é de {} anos').format(m / 4))
if maiorh != 0:
    print('O nome do homem mais velho é {}'.format(nmh))
else:
    print('Não existem homens na lista')
if mcm20a > 1 or mcm20a == 0:
    print('E {} mulheres tem menos de 20 anos'.format(mcm20a))
elif mcm20a == 1:
    print('E apenas {} mulher tem menos de 20 anos'.format(mcm20a))
else:
    print('E Não existem mulheres na lista')
