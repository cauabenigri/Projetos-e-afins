peso_e_nome = []
lista = []
ma_peso = []
me_peso = []
b = 0

while True:

    peso_e_nome.append(str(input('Digite o nome de uma pessoa: ')))
    peso_e_nome.append(int(input('Digite o peso dessa pessoa: ')))
    lista.append(peso_e_nome[:])

    if b == 0:
        me_peso.append(peso_e_nome[:])
        ma_peso.append(peso_e_nome[:])
    else:
        if peso_e_nome[1] > ma_peso[0][1]:
            ma_peso.clear()
            ma_peso.append(peso_e_nome[:])
        elif peso_e_nome[1] < me_peso[0][1]:
            me_peso.clear()
            me_peso.append(peso_e_nome[:])
    if peso_e_nome[1] == ma_peso[0][1] and peso_e_nome != ma_peso[0]:
        ma_peso.append(peso_e_nome[:])
    if peso_e_nome[1] == me_peso[0][1] and peso_e_nome != me_peso[0]:
        me_peso.append(peso_e_nome[:])
    b += 1

    conti = str(input('Quer continuar? [S/N] : ')).upper()
    if conti == 'N':
        break

    peso_e_nome.clear()

print(f'Há {len(lista)} pessoas na lista')
print('As pessoas com menor peso são:')
for c in range(len(me_peso)):
    print(f'{me_peso[c][0]} com {me_peso[c][1]} quilos')
print(f'As pessoas com maior peso são:')
for c in range(len(ma_peso)):
    print(f'{ma_peso[c][0]} com {ma_peso[c][1]} quilos')
