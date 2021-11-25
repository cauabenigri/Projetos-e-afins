f = str(input('Digite uma frase : '))
s = f.split()
r = s[::]
j = ''.join(r)
a = j[::-1]
if a == j:
    print('Sua frase é um palíndromo')
else:
    print('Sua frase não é um palíndromo')
print(s, r, j, a)