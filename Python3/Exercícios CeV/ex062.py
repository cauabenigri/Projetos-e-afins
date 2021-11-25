t = int(input('Qual o primeiro termo?: '))
r = int(input('Qual é a razão?: '))
print(t)
c = t
d = 1
qt = 10
while c < 10:
    t = t + r
    print(t)
    c += 1
while d != 0:
    d = int(input('PAUSA. Quer mais quantos termos?: '))
    c1 = 0
    while c1 < d:
        t = t + r
        c1 = c1 + 1
        print(t)
    qt += d
print('Sessão finalizada com um total de {} termos analisados'.format(qt))