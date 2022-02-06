print('\033[1;35m===== EX 020 =====\033[m')
from random import shuffle

a = str(input('Primeiro nome: '))
b = str(input('Segundo nome: '))
c = str(input('Terceiro nome: '))
d = str(input('Quarto nome: '))

lista = [a,b,c,d]
shuffle(lista)

print(f'A ordem será {lista}')