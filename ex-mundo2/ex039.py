import datetime

print('''Escolha uma das opções abaixo: 
    [ 1 ] Masculino
    [ 2 ] Feminino''')
sexo2 = int(input('Qual o seu sexo? '))

if sexo2 == 2:
    print('\nO alistamento não é obrigatório para você.')
    print('''Deseja prosseguir? 
    [ 1 ] Sim
    [ 2 ] Não''')
    sexo3 = int(input('Escolha uma das opções acima: '))
    if sexo3 == 1:
        print('\nO seu alistamento é de outra forma, prossiga para outra aba do site.')

    elif sexo3 >= 3:
        print('\nOPÇÃO INVÁLIDA')
    else:
        print('\nObrigado pelo acesso.')

elif sexo2 >= 3:
    print('\nOPÇÃO INVÁLIDA')

else:
    print('\033[1;36m-=\033[m' * 30)
    x = int(input('\033[1;35mQual o ano do seu nascimento?\033[m '))
    print('\033[1;36m-=\033[m' * 30)
    y = datetime.date.today().year
    z = y - x

    if z == 18:
        print('\nESTÁ NA HORA DE SE ALISTAR.')
    elif z > 18:
        v = z - 18
        print('\nJÁ PASSOU {} ANOS, VOCÊ JÁ DEVERIA TER SE ALISTADO.'.format(v))
    else:
        b = 18 - z
        print('\nRELAXE, AINDA NÃO CHEGOU A HORA, ESPERE MAIS {} ANO(S).'.format(b))




