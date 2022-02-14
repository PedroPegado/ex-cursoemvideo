print('\033[1;36m-=\033[m'*30)
x = float(input('\033[1;35mQual o valor do imóvel que você deseja comprar?\033[m '))
y = float(input('\033[1;35mQual o seu salário?\033[m '))
z = int(input('\033[1;35mEm quantos anos você quer pagar casa?\033[m '))
print('\033[1;36m-=\033[m'*30)

z2 = z*12
pm = x/z2

if pm <= (y*30)/100:
    print('\033[4;32mAPROVADO!!\033[m '
          'Você pode conceder o empréstimo',end=', ')
else:
    print('\033[4;31mNEGADO!!\033[m '
          'Infelizmente você não poderá conceder o empréstimo',end=', ')
print('O valor pago mensalmente será {:.2f}'.format(pm))


