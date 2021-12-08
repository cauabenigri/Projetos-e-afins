def ficha(nome, gols):
    if '' == nome:
        nome = 'Desconhecido'
    if '' == gols:
        gols = '0'
    print(f'O jogador {nome} fez {gols} gols!')


ficha(str(input('Digite o nome de um jogador: ')), input('Digite quantos gols o jogador fez: '))
