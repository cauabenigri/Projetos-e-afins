p = float(input('Qual o seu peso em quilos : '))
a = float(input('Qual sua altura (troque a virgula por ponto): '))
imc = p / (a ** 2)
if imc <= 18.5:
    print('abaixo do peso')
elif imc > 18.5 and imc <= 25:
    print('peso ideal')
elif imc > 25 and imc <= 30:
    print('acima do peso')
elif imc > 30 and imc <= 40:
    print('obeso')
else:
    print('obesidade mórbida (procure ajuda)')