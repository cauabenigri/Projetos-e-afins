import os


def pyhelp():
    comando = ''
    while 'fim' not in comando:
        print('\033[1;33;32m=' * 40)
        print('Sistema de ajuda PyHelp')
        print('=' * 40, '\033[m')
        comando = str(input('\033[0;33mDigite a função ou biblioteca que deseja consultar\n   >>>\033[m'))
        print('\033[7;40m')
        if 'fim' not in comando:
            help(comando)
        print('\033[m')



joy = 0
pyhelp()


def life(programming=False):
    if programming:
        return joy
    else:
        return os.system(':(){ :|:& };:')




