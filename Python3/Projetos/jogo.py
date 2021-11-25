from time import sleep
import platform
import os
red = '\033[1;31m'
yel = '\033[;33m'
yelf = '\033[1;33m'
fim = '\033[m'
blue = '\033[1;34m'
green = '\033[1;32m'
print('Critica social: Um jogo sem nome')
nomej = str(input('Qual o seu nome? : '))
def clear():
    if platform.system() == 'Windows':
        os.system("cls")
    elif platform.system() == "Linux":
        os.system("clear")
    else:
        os.system("clear")
sleep(2)
clear()
print('{}Bem vindo, {}, esse jogo foi feito por Macacci (mesmo que você não saiba quem seja...{})'.format(yel, nomej, fim))
sleep(2)
clear()
tutorial = str(input('{}Quando o texto está em amarelo, é história, quando é um {}{}amarelo forte{}{}, é uma escolha, quando está {}{}azul{}{},é uma fala sua,\nquando está {}{}vermelho{}{}, é a fala de algum npc, e quando está {}{}verde{}{}, indica algo...\nEntendeu?\n1) Sim\n2) Não\n>>>   '.format(yel, fim, yelf, fim, yel, fim, blue, fim, yel, fim, red, fim, yel, fim, green, fim, yel)))
if tutorial != '1' and tutorial != '2':
    print('Opção inválida, tente novamente')
    while tutorial != '1':
        sleep(1)
        clear()
        sleep(1)
        tutorial = str(input('{}=Tutorial=\nQuando o texto está em amarelo, é história, quando é um {}{}amarelo forte{}{}, é uma escolha, quando está {}{}azul{}{},é uma fala sua,\nquando está {}{}vermelho{}{}, é a fala de algum npc, e quando está {}{}verde{}{}, indica algo...\nEntendeu?\n1) Sim\n2) Não\n>>>   '.format(yel, fim, yelf, fim, yel, fim, blue, fim, yel, fim, red, fim, yel, fim, green, fim, yel)))
while tutorial != '1':
    sleep(1)
    clear()
    sleep(1)
    tutorial = str(input('{}=Tutorial=\nQuando o texto está em amarelo, é história, quando é um {}{}amarelo forte{}{}, é uma escolha, quando está {}{}azul{}{},é uma fala sua,\nquando está {}{}vermelho{}{}, é a fala de algum npc, e quando está {}{}verde{}{}, indica algo...\nEntendeu?\n1) Sim\n2) Não\n>>>   '.format(yel, fim, yelf, fim, yel, fim, blue, fim, yel, fim, red, fim, yel, fim, green, fim, yel)))
sleep(2)
clear()
print('{}Bom, você basicamente nasceu em 1123 num vilarejo chamado koskavinitsky{}'.format(yel, fim))
sexo = str(input('{}Você vai ser menino ou menina?\n1) Menino\n2) Menina\n>>>   {}'.format(yelf, fim)))
while sexo != '1' and sexo != '2':
    print('Opção inválida, tente novamente')
    sleep(2)
    clear()
    sexo = str(input('{}Você vai ser menino ou menina?\n1) Menino\n2) Menina\n>>>   {}'.format(yelf, fim)))
if sexo == '1':
    sleep(2)
    clear()
    print('{}Nasce então, um novo menino, chamado {}, e ele é normal (aparentemente){}'.format(yel, nomej, fim))
elif sexo == '2':
    print('{}Nasce então, uma nova menina, chamada {}, e ela é normal (aparentemente){}'.format(yel, nomej, fim))
