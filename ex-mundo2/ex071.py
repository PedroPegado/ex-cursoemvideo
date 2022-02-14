print('-=' * 20)
print('{:^40}'.format('BANCO DO DRAZIL'))
print('-=' * 20)
din = int(input('Quanto você quer sacar? R$'))
total = din
ced = 50
totalced = 0
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}.')
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('-=' * 20)
print('O BANCO DRAZIL AGRADECE A SUA VISITA. VOLTE SEMPRE.')