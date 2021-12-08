def fatorial(num, show=False):
    f = 1
    for i in range(num, 0, -1):
        f *= i
        if show:
            if i != 1:
                print(i, 'x ', end='')
            else:
                print(i, '= ', end='')
    print(f)


fatorial(5)
