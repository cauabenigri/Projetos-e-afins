dic = {'gols': [], 'total de gols': 0}
dic['nome'] = str(input('Digite o nome do jogador: '))
dic['partidas'] = int(input('Digite a quantidade de partidas jogadas: '))
for i in range(0, dic['partidas']):
    gols = (int(input(f'Digite quantos gols foram feitos na partida {i + 1}: ')))
    dic['gols'].append(gols)
    dic['total de gols'] += gols

print(f'{dic["nome"]} jogou {dic["partidas"]} partidas')
for i in range(0, len(dic['gols'])):
    print(f'Na partida {i + 1}, {dic["nome"]} fez {dic["gols"][i]} gols')
print(f'{dic["nome"]} fez {dic["total de gols"]} gols.')