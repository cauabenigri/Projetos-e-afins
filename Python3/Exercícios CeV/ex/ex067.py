while True:
    num = int(input(f'{ "-" * 40}\nDigite um número para fazermos a tabuada \n{ "-" * 40}\n  >>> '))
    if num < 0:
        break
    for c in range(1, 11):
        tab = num * c
        print(f'{num} x {c} = {tab}')
