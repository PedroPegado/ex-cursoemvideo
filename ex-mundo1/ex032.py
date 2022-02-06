print('\033[1;35m===== EX 032 =====\033[m')

from datetime import date

ano = int(input('Qual ano você quer analisar? Digite 0 se quiser saber do seu ano atual: '))

if ano == 0:
    ano = date.today().year

bi = ano%4
bi2 = ano%100
bi3 = ano%400

if bi == 0 and bi2 != 0 or bi3 == 0:
    print('{} É um ano BISSEXTO.'.format(ano))
else:
    print('{} NÃO é um ano BISSEXTO.'.format(ano))
