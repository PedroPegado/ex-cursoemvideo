cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
        'treze', 'quatorze','quinze', 'desesseis', 'desessete', 'desoito', 'desenove', 'vinte')
num = 0
while True:
        x = int(input('Digite um número de 0 a 20: '))
        if 0 <= x <= 20:
                break
        print('\033[4;31mOPÇÃO INVALIDA, TENTE NOVAMENTE.\033[m')
print(f'\033[1;36mVocê digitou o número {cont[x]}.\033[m')





