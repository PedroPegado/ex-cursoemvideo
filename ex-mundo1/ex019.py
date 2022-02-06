print('\033[1;35m===== EX 019 =====\033[m')
from random import choice

a = str(input('Primeiro nome: '))
b = str(input('Segundo nome: '))
c = str(input('Terceiro nome: '))
d = str(input('Quarto nome: '))

lista = [a,b,c,d]

print(f'O nome escolhido foi {choice(lista)}')
