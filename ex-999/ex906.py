print('='*50)
print('CALCULO SALARIAL'.center(50))
print('='*50)

linha = '=' * 50

def salario():
    ganho_hora = float(input('\nDigite o quanto você ganha por hora: '))
    horas = int(input('\nDigite as horas que você trabalhou no mês: '))
    print(f'\n{linha}')
    salariof = ganho_hora * horas
    print(f'\n\033[1;32m         Seu salário será de {salariof:.2f}R$\033[m')
    print(f'\n{linha}')
salario()

