to18 = toth = mul20 = 0
while True:
    print('-='*20)
    print('          CADASTRO DE PESSOA')
    print('-=' * 20)
    id = int(input('Qual a sua idade? '))
    se = ' '
    while se not in 'MF':
        se = str(input('Qual o seu sexo? [M/F] ')).strip().upper()[0]
    if id >= 18:
        to18 += 1
    if se == 'M':
        toth += 1
    if se == 'F' and id < 20:
        mul20 += 1
    print('-'*40)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total de homens no cadastro é de: {toth}.')
print(f'O total de mulheres com menos de 20 anos é de: {mul20}.')
print(f'O total de pessoas com mais de 18 anos é de: {to18}.')