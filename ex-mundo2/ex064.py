parar = False
soma = 0
cont = 0
while parar == False:
     num = int(input('''\033[1;36mDigite um numero inteiro (Para ver a soma digite '999'):\033[m '''))
     soma += num
     cont += 1
     if num == 999:
          parar = True
          soma = soma - 999
print(f'vc digitou {cont-1} numeros.')
print(f'\033[1;35mA soma de todos os números digitados equivale a\033[m \033[1;32m{soma}\033[m')