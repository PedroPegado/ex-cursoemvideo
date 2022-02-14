def aumentar(preco, taxa):
    p = preco + (preco * taxa/100)
    return p


def diminuir(preco, taxa):
    p = preco - (preco * taxa/100)
    return p


def dobro(preco):
    p = preco * 2
    return p


def metade(preco):
    p = preco / 2
    return p


