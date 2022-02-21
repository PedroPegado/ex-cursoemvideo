print('\033[1;35m===== EX 013 =====\033[m')

def aumento():
    aumento = salario ++ salario/100*15
    print(f'Após o aumento de 15%, seu salário será de R${aumento:.2f}')


salario = float(input('Qual o seu salário atual? '))
aumento()
