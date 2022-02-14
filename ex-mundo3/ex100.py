from random import randint
from time import sleep

def sorteia(lista):
    print('Sorteando nesse caralho:', end=' ')
    for cont in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='')
        sleep(0.25)
    print('ACABOU!')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'somando os valores pares em {lista}, temos {soma}.')



num = list()
sorteia(num)
somaPar(num)