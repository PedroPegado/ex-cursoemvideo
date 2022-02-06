print('\033[1;35m===== EX 031 =====\033[m')

x = (float(input('Qual a distância da sua viagem(em KM)? ')))

vc = 0.50 * x
vl = 0.45 * x

if x <= 200:
    print(f'Você vai pagar R${vc:.2f} na viagem.')
else:
    print(f'Você vai pagar R${vl:.2f} na viagem.')