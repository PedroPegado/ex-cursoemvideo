valores = []
maior = 0
ma = 0
me = 0

for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor para a posição {cont}: ')))
    if cont == 0:
       ma = me = valores[cont]
    elif valores[cont] > ma:
       ma = valores[cont]
    elif valores[cont] < me:
        me = valores[cont]
print(f'Você digitou os valores: {valores}')
print(f'O maior valor foi {ma} na posição ', end='')
for p, v in enumerate(valores):
    if v == ma:
        print(f'{p}... ', end='')
print()
print(f'O menor valor foi {me} na posição ', end='')
for p, v in enumerate(valores):
    if v == me:
        print(f'{p}...', end='')
print()

