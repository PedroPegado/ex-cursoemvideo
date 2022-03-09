print('='*50)
print('PESO IDEAL'.center(50))
print('='*50)

linha = '\033[1;96m=\033[m' * 50

def peso():
    sexo = int(input('''Você é: 
    [ 1 ] Homem
    [ 2 ] Mulher
Digite a número da sua opção: '''))
    print('='*50)
    altura = float(input('\nDigite a sua altura: '))
    print(f'\n{linha}')
    if sexo == 1:
        print(f'\nO peso ideal para você é: {(72.7*altura) - 58:.3f}Kg')
    elif sexo == 2:
        print(f'\nO peso ideal para você é: {(62.1*altura) - 44.7:.3f}Kg')
    print(f'\n{linha}')

peso()