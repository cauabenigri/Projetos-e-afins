from datetime import datetime
ano = datetime.now().year


def voto(adn):
    idade = ano - adn
    if idade < 16:
        return 'negado'
    elif 16 <= idade <= 17 or idade >= 65:
        return 'opcional'
    elif idade >= 18:
        return 'obrigatório'


sit_de_voto = voto(int(input('Digite seu ano de nascimento: ')))
print(f'Sua situação sobre o voto é: {sit_de_voto}')