import random
plv = []
ltr = []
cores = '\033[0;31m', '\033[0;32m', '\033[0;33m', '\033[0;34m', '\033[0;35m', '\033[0;36m', '\033[m'
palavras = [['cingapura', 'marrocos', 'pais de gales'], ['tupac', 'shakira', 'latino'],
            ['guarda chuva', 'ralador', 'machado'], ['balenciaga', 'versace', 'santa cruz']]
tema = random.randint(0, 3)
nmr_palavra = random.randint(0, 2)
palavra = palavras[tema][nmr_palavra]
dif = [8, 6, 3]
for i in range(len(palavra)):
    plv.append('_')
for i in range(0, len(palavra)):
    if ' ' in palavra[i]:
        plv[i] = ' '
print(f'{" ": <5}', 'Jogo da forca\n', '=' * 23)
if tema == 0:
    print(f'{cores[3]}Tema: Países{cores[6]}')
elif tema == 1:
    print(f'{cores[3]}Tema: Cantores{cores[6]}')
elif tema == 2:
    print(f'{cores[3]}Tema: Objetos{cores[6]}')
elif tema == 3:
    print(f'{cores[3]}Tema: Marcas{cores[6]}')
esc = int(input('Digite qual dificuldade você quer jogar: \n[0]Fácil\n[1]Normal\n[2]Difícil\n   >>> '))
while dif[esc] > 0:
    print(f'{cores[0]}Você ainda tem {dif[esc]} tentativas!{cores[6]}')
    print(f'{cores[1]}{plv}{cores[6]}\n')
    letra = str(input(f'{cores[4]}Digite a letra: {cores[6]}'))
    for i in range(0, len(palavra)):
        if letra in palavra[i]:
            plv[i] = letra
    if letra not in palavra:
        dif[esc] -= 1
    ltr.append(letra)
    print('\nLetras digitadas: ', end='')
    for c in ltr:
        print(f'{c}, ', end='')
    print()
    if '_' not in plv:
        print(f'Você ganhou!!! A palavra era {palavra}')
        break
if dif[esc] == 0:
    print(f'Você perdeu!!! A palavra era {palavra}')

