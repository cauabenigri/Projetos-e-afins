def fatorial(num):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f


r = fatorial(5)
print(r)