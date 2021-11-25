lista = list()
conti = 0
while True:
    dic = {'nome': str(input('Digite o nome de um jogador: ')),
           'gols': [],
           'total de gols': 0,
           'total de partidas': int(input(f'Digite quantas partidas ele jogou: '))
           }
    for i in range(0, dic['total de partidas']):
        dic['gols'].append(int(input(f'Digite quantos gols {dic["nome"]} fez na {i + 1} partida: ')))
    for i in dic['gols']:
        dic['total de gols'] += i
    lista.append(dic)
    cont = str(input('Deseja continuar? [S/N]:')).lower()
    while cont != 's' and cont != 'n':
        cont = str(input('Deseja continuar? [S/N]:'))
    if cont == 'n':
        break
print('nº   |   nome   |   total de gols')
for c in range(len(lista)):
    print(f'{c + 1: <6}', end='   ')
    print(f'{lista[c]["nome"]: <13}', end='   ')
    print(lista[c]['total de gols'])
while conti == 0:
    jgdr = int(input('Qual jogador deseja saber o aproveitamento? (0 para sair): ')) - 1
    for i in range(len(lista[jgdr]['gols'])):
        print(f'Na {i + 1}ª partida: ', end='')
        print(lista[jgdr]['gols'][i])
    conti = int(input('Digite 0 para continuar ou qualquer número para parar: '))
