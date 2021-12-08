dicionario = dict()
dicionario['0 a 9'] = ['zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']
dicionario['10 a 19'] = ['dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
                         'dezenove']
dicionario['20 a 90'] = ['vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa']
dicionario['100 a 900'] = ['cem', 'cento', 'duzentos', 'trezentos', 'quatrocentos', 'quinhentos', 'seiscentos',
                           'setecentos', 'oitocentos', 'novecentos']
dicionario1 = dict()
dicionario1['10 a 19'] = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
num = int(input('Digite um número entre 0 e 999: '))

if num > 100:
    print(dicionario['100 a 900'][int(str(num)[0])], 'e ', end='')
    if int(str(num)[1]) == 0:
        print(dicionario['0 a 9'][int(str(num)[2])])
    elif int(str(num)[1]) == 1:
        for i in range(len(dicionario1['10 a 19'])):
            if int(str(num)[1:]) == dicionario1['10 a 19'][i]:
                print(dicionario['10 a 19'][i])
    elif int(str(num)[1]) > 1:
        print(dicionario['20 a 90'][int(str(num)[1]) - 2], 'e ', end='')
        print(dicionario['0 a 9'][int(str(num)[2])])
if 100 > num > 9:
    if int(str(num)[0]) == 1:
        for i in range(len(dicionario1['10 a 19'])):
            if int(str(num)[:]) == dicionario1['10 a 19'][i]:
                print(dicionario['10 a 19'][i])
    elif int(str(num)[0]) > 1:
        print(dicionario['20 a 90'][int(str(num)[0]) - 2], 'e ', end='')
        print(dicionario['0 a 9'][int(str(num)[1])])
if num < 10:
    print(dicionario['0 a 9'][int(str(num)[0])])
