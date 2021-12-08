from random import randint
senha = None
alf = 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
alfm = 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
sim = '@', '#', '!', '$', '%', '&'
num = '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'
leng = int(input('Quantos 4 digitos você quer na senha?: '))
print('Sua senha é: ', end='')
senhastr = list()
for c in range(0, leng):
    senha = f'{alf[randint(0, 25)]}{alfm[randint(0, 25)]}{sim[randint(0, 5)]}{num[randint(0, 9)]}'
    senhastr.append(senha)
print(''.join(senhastr), end='')
listasenha = open('senhas.txt', 'w')
listasenha.write(''.join(senhastr))
