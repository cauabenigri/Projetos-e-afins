s = 0
for c in range(1, 7):
    n = float(input('Digite o {}º valor: '.format(c)))
    if n % 2 == 0:
        s += n
print(s)
