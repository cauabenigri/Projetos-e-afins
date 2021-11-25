times = ('Atlético-MG', 'Palmeiras', 'Flamengo', 'RB Bragantino', 'Fortaleza', 'Internacional', 'Corinthians', 'Fluminense', 'América-MG', 'Atlético-GO', 'São Paulo', 'Ceará', 'Santos', 'Cuiabá', 'Athletico-PR', 'Bahia', 'Sport', 'Juventude', 'Grêmio', 'Chapecoense')
print('\nOs cinco primeiros colocados são: \n')
for c in range(0, 5):
    print(f'{c + 1}º - {times[c]}')
print('\nOs ultimos 4 colocados da tabela são: \n')
for d in range(-4, 0):
    print(f'{d + 21}º - {times[d]}')
c = 0
print('\nA lista em ordem alfabética é: \n')
while c != 20:
    print(f'{c + 1}º - {sorted(times)[c]}')
    c += 1
print(f'\nA Chapecoense está em {times.index("Chapecoense") + 1}º lugar na tabela')