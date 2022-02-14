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



