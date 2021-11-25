def notas(* num, sit=False):
    dic = {'total': len(num),
           'maior nota': max(num),
           'menor nota': min(num),
           'media': 0
    }
    for i in dic.values():
        dic['media'] += i
    dic['media'] /= 2
    if sit:
        if dic['media'] > 7:
            dic['situação'] = 'Boa'
        elif dic['media'] < 7:
            dic['situação'] = 'Ruim'
    return dic


n = notas(2, 4, 5, 6, 7, 6, sit=True)
print(n)
