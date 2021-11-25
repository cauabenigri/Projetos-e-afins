from random import randint
jogo = []
nbr_of_plays = int(input('Quantos palpites você deseja? : '))
print('Aqui estão seus palpites: ')
for c in range(0, nbr_of_plays):
    jogo = [randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60), randint(0, 60)]
    print(jogo)
