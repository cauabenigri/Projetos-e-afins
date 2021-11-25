print('Escolha qual a base para conversão')
e = int(input('[ 1 ] Base binária\n[ 2 ] Base octal\n[ 3 ] Base hexadecimal\n\033[0;31m>>>   \033[m'))
f = int(input('Digite um número para conversão : '))
bin = bin(f)
oct = oct(f)
hex = hex(f)
if e == 1:
    print('{} convertido para binário é {}'.format(f, bin.replace('0b', ' ')))
elif e == 2:
    print('{} convertido para octal é {}'.format(f, oct.replace('0o', ' ')))
elif e == 3:
    print('{} convertido para hexadecimal é {}'.format(f, hex.replace('0x', ' ')))
else:
    print('Opa, esse número não é uma escolha')
