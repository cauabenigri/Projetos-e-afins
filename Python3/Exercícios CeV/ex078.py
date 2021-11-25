var = list()
ma = me = 0
for c in range(0, 5):
    var.append(int(input('Digite um valor: ')))
    if c == 0:
        ma = me = var[c]
    else:
        if var[c] > ma:
            ma = var[c]
        elif var[c] < me:
            me = var[c]
print(f'O maior valor digitado foi {ma} nas posições {var.index(ma) + 1}', end='')
for a in range(var.index(ma) + 1, len(var)):
    if ma == var[a]:
        print(f', {a + 1}')
print(f'O menor foi {me} nas posições {var.index(me) + 1}', end='')
for b in range(var.index(me) + 1, len(var)):
    if me == var[b]:
        print(f', {b + 1}')