p18 = hm = m20 = 0
while True:
    nome = str(input('Digite o nome de uma pessoa: '))
    id = int(input('Digite a idade desta pessoa: '))
    sexo = str(input('Digite o sexo desta pessoa (M para masculino, F para feminino): ')).strip().upper()[0]
    if id > 18:
        p18 += 1
    if sexo == 'F' and id < 20:
        m20 += 1
    if sexo == 'M':
        hm += 1
    cont = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if 'N' in cont:
        break
print(f'{p18} pessoa(s) tem mais de 18 anos, há {hm} homen(s) cadastrados e {m20} mulher(es) tem menos de 20 anos')