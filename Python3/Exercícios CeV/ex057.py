s = str(input('Digite "M" para sexo Masculino e "F" para feminino: ')).strip().upper()[0]
while s not in 'MF':
    s = str(input('Dados inválidos, digite "M" para sexo masculino e "F" para feminino: ')).upper().upper()[0]