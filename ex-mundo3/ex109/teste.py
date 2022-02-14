import moeda

d = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(d)} é {moeda.metade(d, True)}.')
print(f'O dobro de {moeda.moeda(d)} é {moeda.dobro(d, True)}.')
print(f'O aumento de 10% de {moeda.moeda(d)} é {moeda.aumentar(d, 10, True)}.')
print(f'A diminuição de 10% de {moeda.moeda(d)} é {moeda.diminuir(d, 10, True)}.')
