print('\033[1;35m===== EX 015 =====\033[m')

diasp = int(input('Por quantos dias você alugou o carro? '))
kmsp = float(input('Quantos KM você percorreu? '))

dia = diasp*60
km = kmsp*0.15

print(f'Você terá que pagar o valor de R${dia++km:.2f}')