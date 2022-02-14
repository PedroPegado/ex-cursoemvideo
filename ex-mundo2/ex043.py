print('\033[1;36m-=\033[m'*15)
x = float(input('\033[1;35mQual o seu peso?\033[m '))
y = float(input('\033[1;35mQual a sua altura?\033[m '))
print('\033[1;36m-=\033[m'*15)

z = x/(y**2)

if z < 18.5:
    print('Você está abaixo do peso.')
elif z >= 18.5 and z < 25.0:
    print('Você está no peso ideal.')
elif z >= 25.0 and z < 30.0:
    print('Você está sobrepeso.')
elif z >= 30.0 and z < 40:
    print('Você está obeso(a).')
elif z > 40:
    print('Você está na obesidade mórbida, procure ajuda médica.')




