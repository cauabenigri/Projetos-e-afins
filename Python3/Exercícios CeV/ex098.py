from time import sleep


def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if inicio < fim or passo < 0:
        for i in range(inicio, fim, passo):
            print(i, end=' ')
            sleep(0.5)
    elif fim < inicio:
        for i in range(inicio, fim, - passo):
            print(i, end=' ')
            sleep(0.5)
        print(fim)
    print()


contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Digite o início: ')), int(input('Digite o fim: ')), int(input('Digite os passos: ')))
