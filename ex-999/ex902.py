print('='*50)
print('CONVERTER DE CELCIUS PARA FAHRENHEIT'.center(50))
print('='*50)


def converter():
    celcius = int(input('Graus Celcius: '))
    fahren = (celcius * 1.8) + 32
    print(f'Em Fahrenheit, são: {fahren}°')

converter()