def aumentar(preco=0, taxa=0, formato=False):
    p = preco + (preco * taxa/100)
    return p if formato == False else moeda(p)


def diminuir(preco=0, taxa=0, formato=False):
    p = preco - (preco * taxa/100)
    return p if formato == False else moeda(p)


def dobro(preco=0, formato=False):
    p = preco * 2
    return p if formato == False else moeda(p)


def metade(preco = 0, formato=False):
    p = preco / 2
    return p if formato == False else moeda(p)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('=' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('=' * 30)
    print(f'preço analisado: \t{moeda(preco)}')
    print(f'dobro do preço: \t{dobro(preco, True)}')
    print(f'metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(preco, taxar, True)}')
    print('=' * 30)



