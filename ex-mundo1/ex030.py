print('\033[1;35m===== EX 030 =====\033[m')

x = int(input('Digite um número: '))
y = x%2

if y == 0:
    print(f'O número {x} é par')
else:
    print(f'O número {x} é impar')
