import time
import datetime
print('Você quer saber sobre alistamento? ')
time.sleep(2)
a = datetime.date.today().year
i = int(input('Em que ano você nasceu? : '))
falta = 18 - (a - i)
passou = 18 + (i - a)
passo = passou * -1
if a - i < 18:
    print('Você ainda vai ter que se alistar daqui a {} anos'.format(falta))
elif a - i == 18:
    print('Esse ano vc ja tem q se alistar')
else:
    print('Já passou {} anos desde o que você deveria se alistar'.format(passo))