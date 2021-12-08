def escreva(txt):
    print('~' * (len(txt) + 2))
    print(f' {txt.title()} ')
    print('~' * (len(txt) + 2))


escreva(str(input('Digite um título: ')))
