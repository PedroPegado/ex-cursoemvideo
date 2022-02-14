import time

x = int(input('\033[1;36mDigite um número inteiro:\033[m '))
print('''\033[1;35;46mEscolha uma das opções abaixo:\033[m
\033[1;36m[ 1 ] BINÁRIO
[ 2 ] OCTAL
[ 3 ] HEXADECIMAL\033[m''')
y = int(input('\033[1;36mQual opção você quer:\033[m '))
print('\nConvertendo',end='')
time.sleep(0.5)
print('.',end='')
time.sleep(0.5)
print('.',end='')
time.sleep(0.5)
print('.',end=' ')
time.sleep(0.5)


if y == 1:
    print('\033[1;35mO número {} em\033[1;34m BINÁRIO\033[m \033[1;35mé {}\033[m'.format(x,bin(x)[2:]))
elif y == 2:
    print('\033[1;35mO número {} em\033[1;31m OCTAL\033[m \033[1;35mé {}\033[m'.format(x,oct(x)[2:]))
elif y == 3:
    print('\033[1;35mO número {} em\033[1;35m \033[1;32mHEXADECIMAL\033[m \033[1;35mé {}\033[m'.format(x,hex(x)[2:]))
else:
    print('\033[4;31mOpção inválida. Tente novamente.\033[m')


