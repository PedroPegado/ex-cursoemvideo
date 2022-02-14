valor = []
while True:
    x = valor.append(int(input('Digite um valor: ')))

    y = str(input('quer continuar ? S ou N? ')).strip().upper()[0]
    if y in 'Nn':
        break

valor.sort(reverse=True)
print(f'Foram digitados {len(valor)} números.')
print(f'Os numeros em ordem decrescente: {valor}.')
if 5 in valor:
    print('5 está na lista.')
else:
    print('5 não apareceu na lista.')
