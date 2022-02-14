valor = []
par = []
impar = []
y = ''
while True:
    x = (int(input('Digite um valor: ')))
    valor.append(x)
    if x % 2 == 0:
        par.append(x)
    elif x % 2 == 1:
        impar.append(x)

    y = str(input('quer continuar ? S ou N? ')).strip().upper()[0]
    if y in 'Nn':
        break
print(f'Os números da lista são {valor}.')
print(f'Os pares da lista são {par}.')
print(f'Os ímpares da lista são {impar}.')



