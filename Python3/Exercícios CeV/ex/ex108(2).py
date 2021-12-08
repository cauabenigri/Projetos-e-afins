from ex108 import moeda
import ex107

num = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda(num)} é {moeda(ex107.dobro(num=num))}')
print(f'A metade de {moeda(num)} é {moeda(ex107.metade(num=num))}')
print(f'O aumento de 12% a {moeda(num)} é {moeda(ex107.aumento(num=num, porcento=12))}')
print(f'Diminuindo 10% de {moeda(num)} temos {moeda(ex107.diminui(num=num, porcento=12))}')
