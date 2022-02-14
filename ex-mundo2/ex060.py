#import math
#x = int(input('Qual número deseja fatorar? '))
#f = math.factorial(x)
#print(f'O fatorial de {x} é {f}')

num = int(input('Qual número deseja fatorar? '))
c = num
f = 1
print(f'calculando {num}!',end=' = ')
while c > 0:
    print(f'{c}', end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f'{f}')

#num = int(input('Digite um numero: '))
#f = 1
#c = num
#while c > 0:
    #print(f'{c}',end='')
    #print(' x ' if c > 1 else ' = ',end='')
    #f *= c
    #c -= 1
#print(f'{num} em fatorial passa a ser: {f}!' )


