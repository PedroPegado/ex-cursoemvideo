print('\033[1;35m===== EX 035 =====\033[m')

print('\033[1;36m-=\033[m'*20)
print('\033[1;36m       ANALISADOR DE TRIÂNGULOS\033[m')
print('\033[1;36m-=\033[m'*20)

x = float(input('\033[1;35mO 1° segmento: \033[m'))
y = float(input('\033[1;35mO 2° segmento: \033[m'))
z = float(input('\033[1;35mO 3° segmento: \033[m'))

if x < y + z and y < x + z and z < x + y:
    print('\033[4;32mÉ POSSÍVEL\033[m fazer um triângulo.')
else:
    print('\033[4;31mNÃO É POSSÍVEL\033[m fazer um triângulo.')