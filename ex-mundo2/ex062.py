x = int(input('Digite o primeiro termo: '))
y = int(input('Digite a razão: '))
cont = 0
termo2 = 10
total = 0
while termo2 != 0:
    total += termo2
    while cont <= total:
        print(x, end=' ')
        x += y
        cont += 1
    termo2 = int(input('\nQuantos termos a mais: '))
print('\033[4;31mPrograma finalizado.\033[m')
