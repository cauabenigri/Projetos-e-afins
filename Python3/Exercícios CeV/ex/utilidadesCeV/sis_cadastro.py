import os
from time import sleep


def clear():
    if 'nt' in os.name:
        os.system('cls')
    else:
        os.system('clear')


def banner(title):
    print('\033[0;33m', '-' * len(title) * 2)
    print('\t', title)
    print('-' * len(title) * 2, '\033[m')


def cadastro():
    vali_nome = vali_idade = False
    opn = open('Pessoas_cadastradas.txt', 'a+')
    while not vali_nome:
        try:
            nome = str(input('Digite o nome da pessoa: '))
        except:
            print('Erro, digite um nome válido!')
        else:
            vali_nome = True
    while not vali_idade:
        try:
            idade = int(input('Digite a idade da pessoa: '))
        except:
            print('Erro, digite uma idade válida!')
        else:
            vali_idade = True
    opn.write(f'\n{nome.title(): <20}\t{idade} anos')
    opn.read()
    print('Pessoa cadastrada com sucesso!')


def escolha(title):
    quit = cont = False
    while not quit:
        clear()
        banner(title)
        while not cont:
            try:
                esc = int(input('[1] Cadastrar uma pessoa\n[2] Ver a lista\n[3] Limpar a lista\n[4] Sair\n >>>'))
            except:
                print('Erro! Digite um valor valido!')
            else:
                cont = True
        while esc != 1 and esc != 2 and esc != 3:
            esc = int(input('Erro!\n[1] Cadastrar uma pessoa\n[2] Ver a lista\n[3] Limpar a lista\n[4] Sair\n >>>'))
        if esc == 1:
            cadastro()
        elif esc == 2:
            print('''__________________________________
        PESSOAS CADASTRADAS
__________________________________''')
            print(open('Pessoas_cadastradas.txt').read())
        elif esc == 3:
            open('Pessoas_cadastradas.txt', 'w').flush()
            print('Lista limpa com sucesso!')
            sleep(1.5)
        else:
            quit = True
        sleep(2)
        cont = False