tupla = ('caralho', 'porra', 'putaquepariu', 'sefude', 'pika')

for p in tupla:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')