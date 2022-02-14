print('===== LOJA DO DRAZILZINHO =====')
x = float(input('Qual o preço do produto? R$'))
print('''\nEscolha a sua forma de pagamento
[ 1 ] À vista no dinheiro (10% de desconto)
[ 2 ] À vista no cartão (5% de desconto)
[ 3 ] 2x no cartão (preço formal)
[ 4 ] 3x ou mais no cartão (20% de juros)''')
y = int(input('Qual a opção desejada? '))
if y == 1:
    print('\nO valor será de R${:.2f}'.format(x-(x/100)*10))
elif y == 2:
    e = (x / 100) * 5
    r = x - e
    print(f'\n\033[1;36mO valor com desconto aplicado vai de R${x:.2f} para R${r:.2f}\033[m')
elif y == 3:
    print('\nO valor será pago em 2x de R${:.2f}, o valor total é de R${:.2f}'.format(x/2, x))
elif y == 4:
    p = int(input('Em quantas parcelas? '))
    print('O valor pago em {}x será de R${:.2f}, já que o valor total é de R${:.2f}'.format(p, (x+(x/100*20))/p, (x+(x/100*20))))
else:
    print('\033[1;31mOPÇÃO INVÁLIDA. TENTE NOVAMENTE.\033[m')



