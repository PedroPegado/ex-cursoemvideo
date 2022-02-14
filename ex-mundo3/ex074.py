from random import randint

x = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram: ',end='')
for n in x:
    print(f'{n} ',end='')
print(f'\nO maior valor foi {max(x)}')
print(f'O menor valor foi {min(x)}')