sit = {}
sit['nome'] = str(input('Digite o nome do aluno: '))
sit['nota'] = float(input('Digite a nota do aluno: '))
if sit['nota'] >= 7:
    sit['situação'] = 'aprovado'
else:
    sit['situação'] = 'reprovado'
print(f'O aluno {sit["nome"]} foi {sit["situação"]}')