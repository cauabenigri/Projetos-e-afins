from random import randint
a = randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10)
for c in a:
    print(c, end=' ')
print(f'\nO maior número foi {max(a)}, e o menor foi {min(a)}')