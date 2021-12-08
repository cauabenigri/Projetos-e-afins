import datetime
ano = datetime.datetime.now().year
dic = dict()
dic['nome'] = str(input('Digite seu nome: '))
num = int(input('Digite o ano de nascimento: '))
dic['idade'] = ano - num
dic['ct'] = int(input('Digite sua carteira de trabalho: '))
if dic['ct'] != 0:
    dic['ano de contratação'] = int(input('Digite o ano de sua contratação: '))
    dic['salário'] = float(input('Digite seu salário: '))
    dic['aposentadoria'] = dic['ano de contratação'] - num + 35
for c in dic.keys():
    print(f'O(a) {c} é {dic[f"{c}"]}')
