import datetime
atual = datetime.date.today().year
pessoas = 0
pessoasme = 0
for c in range(1, 8):
    ano = int(input(f'Em que ano a {c}° pessoa nasceu? '))
    idade = atual - ano
    if idade >= 21:
        pessoas = pessoas + 1
    elif idade < 21:
        pessoasme = pessoasme + 1

print(f'{pessoas} pessoas são maiores de idade e {pessoasme} pessoas são menores de idade.')

