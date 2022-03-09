"""
Faça um programa que peça o raio de um círculo, calcule e mostre sua área.


Área = π(3.14) * raio²


Exemplo:

Entrada  ->  Saída

10           314cm² 
"""
from time import sleep


print('='*50)
print('CALCULADORA DE RAIO'.center(50))
print('='*50)

def areacirc():
    raio = float(input('\n\033[1;34mDigite o raio do seu círculo(em cm): \033[m'))
        
    area = 3.14*(raio**2)
    linha = '\033[1;96m=\033[m' * 50
    while True:
        if raio == ' ':
            print('Digite um número.')
        else: 
            print(f'\n{linha}')
            print(f'\n\033[1;96m     o seu círculo contém a área de \033[1;31m{area:.2f}cm²\033[m\033[m')
            print(f'\n{linha}')
            break
    sleep(3)
    while True:
        print(f'\n{linha}')
        convert = int(input("""\n\033[1;31mQuer converter sua área para metros quadrados?

    [ 1 ] Sim
    [ 2 ] Não

Digite o número de acordo com sua opção: \033[m"""))
        print(f'\n{linha}')
        if convert == 1: 
            print(f'\n{linha}')
            print(f'\n\033[1;96m     o seu círculo contém a área de \033[1;31m{area/10000:.2f}m²\033[m\033[m')
            print(f'\n{linha}')
            print('\n\033[1;32mOBRIGADO POR CALCULAR CONOSCO, VOLTE SEMPRE.\033[m')
            break
        else:
            print('\n\033[1;32mOBRIGADO POR CALCULAR CONOSCO, VOLTE SEMPRE.\033[m')
            break
        
areacirc()








