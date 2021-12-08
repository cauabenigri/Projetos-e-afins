from ex108 import moeda
import ex109

num = float(input('Digite um valor: R$'))
print(f'O dobro de {moeda(num)} é {ex109.dobro(num, bool=True)}')
print(f'A metade de {moeda(num)} é {ex109.metade(num)}')
print(f'O aumento de 12% a {moeda(num)} é {ex109.aumento(num, 12, bool=True)}')
print(f'Diminuindo 10% de {moeda(num)} temos {ex109.diminui(num, 12)}')