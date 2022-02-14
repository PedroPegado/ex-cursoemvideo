cont = 0
x = int(input('Digite um número: '))
y = int(input('Digite outro número: '))
z = int(input('Digite mais um: '))
c = int(input('Digite o último: '))
tuplas = (x, y, z, c)
if 3 in tuplas:
    tuplas.index(3)+1
else:
    print('O numero 3 não aparece nenhuma vez')


#print(f'O número 9 apareceu {tuplas.count(9)} vezes.')
#print(f'O primeiro 3 apareceu na {tuplas.index(3)+1}° posição')

