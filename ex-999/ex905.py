print('='*50)
print('CALCULADORA DE ÁREA DO QUADRADO'.center(50))
print('='*50)

linha = '\033[1;96m=\033[m' * 65

def areaquad():
    medida = int(input('''O seu quadrado está em que medida: 
    [ 1 ] Centimetros(cm)
    [ 2 ] Metros(m)
    [ 3 ] Quilometros(km)
-> Escolha o número de sua opção: '''))

    lado = float(input('\n-> Quanto mede o lado deste quadrado: '))
    print('='*50)
    area = (lado*lado)
    area2 = area*2

    print(f'\n{linha}')
    if medida == 1:
        print(f'\n\033[1;31mEsse quadrado tem a área de {area:.2f}cm² e o seu dobro é {area2:.2f}cm²\033[m')
    elif medida == 2:
        print(f'\n\033[1;31mEsse quadrado tem a área de {area:.2f}m² e o seu dobro é {area2:.2f}m²\033[m')
    elif medida == 3:
        print(f'\n\033[1;31mEsse quadrado tem a área de {area:.2f}km² e o seu dobro é {area2:.2f}km²\033m')
    print(f'\n{linha}')

areaquad()
