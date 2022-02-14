import moeda

d = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(d)} é {moeda.moeda(moeda.metade(d))}.')
print(f'O dobro de {moeda.moeda(d)} é {moeda.moeda(moeda.dobro(d))}.')
print(f'O aumento de 10% de {moeda.moeda(d)} é {moeda.moeda(moeda.aumentar(d, 10))}.')
print(f'A diminuição de 10% de {moeda.moeda(d)} é {moeda.moeda(moeda.diminuir(d, 10))}.')
