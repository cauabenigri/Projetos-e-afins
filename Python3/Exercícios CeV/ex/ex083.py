lista = list()
parentesesesq = parentesesdir = 0
ex = str(input('Digite a expressão: ')).replace('', ' ')
exs = ex.split()
for car in exs:
    lista.append(car)
for carac in lista:
    if carac == '(':
        parentesesesq += 1
    if carac == ')':
        parentesesdir += 1
if parentesesdir == parentesesesq:
    print('A expressão está valida')
else:
    print('A expressão está inválida')
