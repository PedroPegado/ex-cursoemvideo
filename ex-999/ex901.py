"""
Faça um programa que peça dois números e imprima a soma.

a + b = c

EXEMPLO:

entrada  ->  saída
 2 + 2         4
"""
print('='*50)
print('SOME DOIS NÚMEROS'.center(50))
print('='*50)

linha = '\033[1;96m=\033[m' * 50

def soma():
    num1 = float(input('\n\033[1;34mEscreva o primeiro número: \033[m'))
    num2 = float(input('\033[1;34mEscreva o segundo número: \033[m'))
    resultado = num1 + num2

    print(f'\n{linha}')
    print(f'\n\033[1;31m A soma dos números é igual a {resultado:.2f}')
    print(f'\n{linha}')
    print('\n\033[1;32mOBRIGADO POR CALCULAR CONOSCO, VOLTE SEMPRE.')

soma()
