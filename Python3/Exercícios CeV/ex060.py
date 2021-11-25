n = int(input('Digite um número para fazermos o fatorial: ')) + 1
f = 1
while n > 1:
    n = (n - 1)
    f = f * n
print('O fatorial de {} é igual á = {}'.format(n, f))