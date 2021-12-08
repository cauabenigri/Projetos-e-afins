lista = list()
media = 0
m = False
while True:
    dic = dict()
    dic['nome'] = str(input('Digite o nome de uma pessoa: '))
    dic['sexo'] = str(input('Digite o sexo dessa pessoa [M/F]: ')).lower()
    while dic['sexo'] != 'm' and dic['sexo'] != 'f':
        dic['sexo'] = str(input('Digite o sexo dessa pessoa [M/F]: ')).lower()
    dic['idade'] = int(input('Digite a idade dessa pessoa: '))
    lista.append(dic)
    print(lista)
    cont = str(input('Deseja continuar? [S/N]: ')).lower()[0]
    while cont != 'n' and cont != 's':
        cont = str(input('Deseja continuar? [S/N]: '))
    if cont == 'n':
        break
print(f'{len(lista)} pessoas foram cadastradas.')
for i in range(len(lista)):
    media += lista[i]['idade']
    if 'f' in lista[i]['sexo']:
        m = True
print(f'A média de idade do grupo é {media / len(lista)}')
if m:
    print('A lista de mulheres é:')
    for i in range(len(lista)):
        if 'f' in lista[i]['sexo']:
            print(lista[i]['nome'])
print(f'As pessoas com idade acima da média são: ')
for i in range(len(lista)):
    if lista[i]['idade'] > media / 2:
        print(lista[i]['nome'])
