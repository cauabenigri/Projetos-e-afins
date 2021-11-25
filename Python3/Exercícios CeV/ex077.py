list = 'jovem', 'bicicleta', 'chiclete', 'bola', 'idoso'
a = 0
d = 'a', 'e', 'i', 'o', 'u'
for c in range(len(list)):
    b = list[c]
    print(f'Em {b[0:]}, tem as vogais: ')
    for f in range(len(b)):
        for e in range(len(d)):
            if d[e] in b[f]:
                print(d[e])
