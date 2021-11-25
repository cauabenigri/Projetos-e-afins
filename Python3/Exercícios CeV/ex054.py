import datetime
a = datetime.date.today().year
co = 0
for c in range(1, 8):
    i = int(input('Qual a data de nascimento da {}ª pessoa : '.format(c)))
    if a - i >= 21:
        co = co + 1
if co > 1:
    print('{} pessoas atingiram a maior idade e {} são menores (maior idade = 21)'.format(co, 7 - co))
else:
    print('{} pessoa atingiu a maior idade e {} são menores (maior idade = 21)'.format(co, 7 - co))
