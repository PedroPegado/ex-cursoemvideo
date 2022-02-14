print('\033[1;36m-=\033[m'*16)
x = float(input('\033[1;35mEscreva a sua primeira nota:\033[m '))
y = float(input('\033[1;35mEscreva a sua segunda nota:\033[m '))
print('\033[1;36m-=\033[m'*16)

z = (x+y)/2

if z > 5.0 and z < 6.9:
    print('RECUPERAÇÃO')
elif z < 5.0:
    print('REPROVADO')
elif z >= 7.0:
    print('APROVADO')
