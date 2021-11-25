a = int(input('Digite um número para descobrirmos os primeiros termos da sequência de fibonacci: '))
b = 1
c = 0
cont = 3
print('0 -> 1 -> ', end='')
while cont <= a:
    d = b + c
    c = b
    b = d
    cont = cont + 1
    print(d, end=' -> ')
print(' FIM!')