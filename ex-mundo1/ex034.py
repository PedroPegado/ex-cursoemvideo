print('\033[1;35m===== EX 034 =====\033[m')

sala = float(input('Qual o seu salário? R$'))

sm = (sala / 100) * 15
sg = (sala / 100) * 10
nsm = sm + sala
nsg = sg + sala

if sala > 1250:
    print(f'Seu novo salário é R${nsg:.2f}')
else:
    print(f'Seu novo salário é R${nsm:.2f}')