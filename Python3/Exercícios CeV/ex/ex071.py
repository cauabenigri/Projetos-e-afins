nota = 50
totnota = 0
val = int(input(f'{"-" * 15}\n{"     banco"}\n{"-" * 15}\nQual valor deseja retirar?: R$'))
while True:
    if nota <= val:
        val -= nota
        totnota += 1
    else:
        print(f'{totnota} de {nota}')
        if val < 50:
            nota = 20
            totnota = 0
        if val < 20:
            nota = 10
            totnota = 0
        if val < 10:
            nota = 1
            totnota = 0
        if val == 0:
            break
