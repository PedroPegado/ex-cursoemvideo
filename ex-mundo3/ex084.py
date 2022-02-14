dado = []
galera = []
menor = 0
maior = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    elif dado[1] < menor:
        menor = dado[1]
    elif dado[1] > maior:
        maior = dado[1]
    galera.append(dado[:])
    dado.clear()
    y = str(input('quer continuar ? [S/N]: ')).strip().upper()[0]
    if y in 'Nn':
        break
print(f'O total de pessoas cadastradas foram: {len(galera)}')
print(f'O maior peso foi {maior}Kg. Peso de ', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso foi {menor}Kg. Peso de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'[{p[0]}]', end='')
print()