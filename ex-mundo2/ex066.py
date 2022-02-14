num = soma = cont = 0

while True:
     num = int(input('''\033[1;36mDigite um numero inteiro (Para ver a soma digite '999'):\033[m '''))
     if num == 999:
          break
     soma += num
     cont += 1

print(f'\033[1;35mvc digitou {cont} numeros. \033[m', end='')
print(f'\033[1;35mA soma de todos os números digitados equivale a\033[m \033[1;32m{soma}\033[m')