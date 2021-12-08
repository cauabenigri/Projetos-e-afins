import random
sorteio = []
dic = {}

# sorteio

for a in range(1, 5):
    dic[f'jogador {a}'] = random.randint(1, 6)
    sorteio.append(dic[f'jogador {a}'])
for j, v in dic.items():
    print(f'O jogador {j} tirou {v}')

# ranking

print('=' * 30)
print(f'{"": ^10}Ranking')
print('=' * 30)
for c, i in enumerate(sorted(dic, key=dic.get, reverse=True)):
    print(f'Em {c + 1}º lugar:')
    print(i, 'com', end=' ')
    print(dic[f'{i}'])
