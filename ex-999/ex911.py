linha = '\033[1;96m=\033[m' * 50
print(linha)
print('LOJA DE TINTAS 2.0'.center(50))
print(linha)

import math
from traceback import print_tb

def tintas():
    metros = float(input('Digite o tamanho da sua parede em metros quadrados(m²): '))
    litros = metros/3
    latas = round(litros / 18)
    galoes = round(litros / 3.6)
    preco_lata = latas * 80
    preco_galoes = galoes * 25
    latas_mistas18 = ((litros * 0.10) + litros) / 18
    litros18 = math.trunc(latas_mistas18) * 18
    resto18 = ((litros * 0.10) + litros) - litros18
    latas_mistas36 = resto18 / 3.6
    misto_todo = math.trunc(latas_mistas18) + math.ceil(latas_mistas36)
    misto_preco18 = math.trunc(latas_mistas18) * 80
    misto_preco36 = math.ceil(latas_mistas36) * 25
    total_mistos = misto_preco18 + misto_preco36
     
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
            print(f'''LATAS DE 18 LITROS: {math.trunc(latas_mistas18)}
GALÕES DE 3,6 LITROS: {math.ceil(latas_mistas36)}
VALOR TOTAL(com 10% de quebra): {total_mistos}''')

        elif escolha == 4:
            break
        print(linha)
        sair = int(input('''
        [ 1 ] ESCOLHER OUTRA OPÇÃO
        [ 2 ] SAIR DO PROGRAMA
        Opção: '''))
        if sair == 1:
            continue
        else:
            break

tintas()
