import moeda

d = float(input('Digite o preço: R$'))
print(f'A metade de {d} é {moeda.metade(d)}.')
print(f'O dobro de {d} é {moeda.dobro(d)}.')
print(f'O aumento de 10% de {d} é {moeda.aumentar(d, 10)}.')
print(f'A diminuição de 10% de {d} é {moeda.diminuir(d, 10)}.')
