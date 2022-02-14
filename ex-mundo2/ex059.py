from time import sleep
opcao = 0
n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
while opcao != 5:
    print('''    [ 1 ] SOMAR
    [ 2 ] MULTIPLICAR
    [ 3 ] MAIOR
    [ 4 ] NOVOS NÚMEROS 
    [ 5 ] SAIR DO PROGRAMA''')
    opcao = int(input('Qual a opção que deseja? '))
    if opcao == 1:
        soma = n1 + n2
        print(f'a soma entre {n1} e {n2} é igual a {soma}!')
    elif opcao == 2:
        multi = n1 * n2
        print(f'A multiplicação entre {n1} e {n2} é igual a {multi}!')
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2}, o maior valor é {maior}!')
    elif opcao == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizando o programa...')
    else:
        print('OPÇÃO INVÁLIDA. TENTE NOVAMENTE.')
    print('=-='*10)
    sleep(1)
print('Fim do programa, volte sempre!')

