print('='*50)
print('PEIXES DO João Papo-de-Pescador'.center(50))
print('='*50)

linha = '=' * 50

def peixes():
    peso = float(input('\nDigite a quantidade de kilos de peixe: '))
    if peso <= 50:
        print(linha)
        print('''\nA quantidade de peso está menor que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos), você não precisará pagar nada.
        
OBRIGADO PELO ACESSO.''')
        print(linha)
    else:
        excesso = peso - 50
        multa = excesso * 4
        print(linha)
        print(f'''\nA quantidade de peso está maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos), você ultrapassou {excesso}Kg do permitido e terá que pagar a multa de \033[1;31m{multa}R$\033[m
        
OBRIGADO PELO ACESSO.''')
print(linha)

peixes()
