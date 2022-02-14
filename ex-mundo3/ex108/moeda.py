def aumentar(preco=0, taxa=0):
    p = preco + (preco * taxa/100)
    return p


def diminuir(preco=0, taxa=0):
    p = preco - (preco * taxa/100)
    return p


def dobro(preco=0):
    p = preco * 2
    return p


def metade(preco = 0):
    p = preco / 2
    return p


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:>.2f}'.replace('.', ',')



