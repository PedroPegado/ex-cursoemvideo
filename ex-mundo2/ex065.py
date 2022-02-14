parar = False
soma = 0
cont = 0
while parar == False:
     num = int(input('''\033[1;36mDigite um numero inteiro:\033[m '''))
     soma += num
     cont += 1
     print('''Deseja continuar?
     [ 1 ] SIM
     [ 2 ] NÃO''')
     opcao = int(input('Escolha sua opção: '))
     if opcao == 2:
          parar = True
     elif opcao == 1:
          parar = False
     else:
          print('OPÇÃO INVALIDA.')
media = soma/cont
print(f'A média é {media}')
