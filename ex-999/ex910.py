linha = '\033[1;96m=\033[m' * 50
print(linha)
print('LOJA DE TINTAS'.center(50))
print(linha)


def tintas():
    metros = float(input('Digite o tamanho da sua parede em metros quadrados(m²): '))
    litros = metros/3
    latas = litros/18
    preco = latas * 80
    print(linha)
    print(f'''Você precisará de {latas:.2f} latas de tinta.
Você gastará {preco:.2f}R$.''')
    print(linha)


tintas()
