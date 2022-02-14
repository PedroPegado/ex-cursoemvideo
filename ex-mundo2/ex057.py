#n = ''
#while n != 'MnFf':
    #print('Qual o seu sexo? ')
    #x = input('[M/F]').upper().strip()
    #if x in 'MmFf':
        #print('OBRIGADO PELO ACESSO.')
    #else:
        #print('TENTE NOVAMENTE, INVALIDO.')


sexo = str(input('Qual seu SEXO?: [M/F] ')).strip()
while sexo not in 'FfMm':
        sexo = str(input('Opção invalida.Tente novamente.\nQual seu SEXO?: [M/F]'))
if sexo in 'Mm':
        print(f'Homao da porra em rs')
else:
        print(f'Rabudinha em princesa')
