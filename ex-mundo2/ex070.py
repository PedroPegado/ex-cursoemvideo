print('-='*20)
print('          LOJINHA DO DRAZIL')
print('-='*20)
total = totmil = menor = cont = 0
barato = ''
while True:
    prod = str(input('Qual o produto? ')).strip()
    pre = float(input('Qual o preço? R$'))
    cont += 1
    total += pre
    if pre > 1000:
        totmil += 1
    if cont == 1 or pre < menor:
        menor = pre
        barato = prod
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total gasto foi R${total:.2f}.')
print(f'{totmil} produtos custando mais que R$1.000.')
print(f'O produto mais barato foi {barato} e custa R${menor:.2f}.')
