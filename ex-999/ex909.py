linha = '\033[1;96m=\033[m' * 50
print(linha)
print('CALCULO SALARIAL COM DESCONTOS'.center(50))
print(linha)



def salario():
    ganho_hora = float(input('\nDigite o quanto você ganha por hora: '))
    horas = int(input('\nDigite as horas que você trabalhou no mês: '))
    print(f'\n{linha}')
    bruto = ganho_hora * horas
    ir = (11/100) * bruto
    inss = (8/100) * bruto
    sindicato = (5/100) * bruto
    liquido = bruto - (ir + inss + sindicato)
    print(f'\n{linha}')
    print(f'\nSALÁRIO BRUTO: {bruto:.2f}R$')
    print(f'PAGAMENTO DO IMPOSTO DE RENDA: {ir:.2f}R$')
    print(f'PAGAMENTO DO INSS: {inss:.2f}R$')
    print(f'PAGAMENTO DO SINDICATO: {sindicato:.2f}R$')
    print(f'SALÁRIO LÍQUIDO: {liquido:.2f}R$')
    print(f'\n{linha}')

    
salario()
