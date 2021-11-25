nome_e_nota = []
boletim = []
media = []

while True:

    nome_e_nota.append(str(input('Digite o nome do aluno:')))
    nome_e_nota.append(float(input('Digite a 1ª nota: ')))
    nome_e_nota.append(float(input('Digite a 2ª nota: ')))
    media.append((nome_e_nota[1] + nome_e_nota[2]) / 2)
    boletim.append(nome_e_nota[:])
    nome_e_nota.clear()

    conti = str(input('Quer continuar? [S/n] : ')).lower()
    if conti == 'n':
        break

print('=' * 40)
print('  Nº  |   Nome    |  Média  ')
print('=' * 40)

for c in range(len(boletim)):
    print(f'  {c}       {boletim[c][0]: <11}', end='')
    print(f'{media[c]}')
print('=' * 40)

while True:
    aluno = int(input('Digite o número do aluno que deseja saber as notas, ou 999 para interromper: '))
    if aluno == 999:
        break
    for i in range(len(boletim)):
        if aluno == i:
            print(f'O aluno {boletim[aluno][0]} tirou as notas {boletim[aluno][1]} e {boletim[aluno][2]}')
