def area(larg, comp):
    a = larg * comp
    print(f'A área de um terreno {larg}x{comp} é igual a {a}m².')


print('CONTROLE DE TERRENOS')
print('-=' * 10)
l = float(input('Qual a largura? '))
c = float(input('Qual o comprimento? '))
area(l, c)





