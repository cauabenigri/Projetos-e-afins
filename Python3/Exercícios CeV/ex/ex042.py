s1 = float(input('Qual o primeiro segmento? : '))
s2 = float(input('Qual o segundo segmento? : '))
s3 = float(input('Qual o terceiro segmento? : '))
if s1 < s3 + s2 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Pode formar um triângulo', end='')
    if s1 == s2 == s3:
        print(' equilátero')
    elif s1 != s2 != s3 and s1 != s3:
        print(' escaleno')
    elif s1 == s2 != s3 or s2 == s3 != s1 or s3 == s1 != s2:
        print(' isóceles')
else:
    print('Não pode formar um trângulo')