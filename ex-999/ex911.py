linha = '\033[1;96m=\033[m' * 50
print(linha)
print('LOJA DE TINTAS 2.0'.center(50))
print(linha)

import math
from traceback import print_tb

def tintas():
    metros = float(input('Digite o tamanho da sua parede em metros quadrados(m²): '))
    litros = metros/3
    latas = math.ceil(litros / 18)
    galoes = math.ceil(litros / 3.6)
    preco_lata = latas * 80
    preco_galoes = galoes * 25
    while True:
        print(linha)
        escolha = int(input('''\nESCOLHA A FORMA QUE DESEJA COMPRAR:

    [ 1 ] APENAS LATAS
    [ 2 ] APENAS GALÕES
    [ 3 ] LATAS E GALÕES
    [ 4 ] SAIR

Digite o número da sua escolha: '''))
        print(linha)
        if escolha == 1:
            print(f'''QUANTIDADE DE LATAS: {latas}
            PREÇO: {preco_lata}R$''')
            
        elif escolha == 2:
            print(f'''QUANTIDADE DE LATAS: {galoes}
            PREÇO: {preco_galoes}R$''')
        
        elif escolha == 3:
            

        elif escolha == 4:
            break

        sair = int(input('''
        [ 1 ] ESCOLHER OUTRA OPÇÃO
        [ 2 ] SAIR DO PROGRAMA'''))
        if sair == 1:
            continue
        else:
            break

tintas()
