import datetime

print('\033[1;36m-=\033[m'*16)
ano = int(input('\033[1;35mQual seu ano de nascimento?\033[m '))
print('\033[1;36m-=\033[m'*16)

y = datetime.date.today().year
ano2 = y-ano

if ano2 <= 9:
    print('Sua categoria é a \033[1;32mMIRIM!!\033[m')
elif ano2 > 9 and ano2 <= 14:
    print('Sua categoria é a \033[1;32mINFANTIL!!\033[m')
elif ano2 > 14 and ano2 <= 19:
    print('Sua categoria é a \033[1;32mJUNIOR!!\033[m')
elif ano2 <= 25:
    print('Sua categoria é a \033[1;32mSÊNIOR!!\033[m')
elif ano2 > 25:
    print('Sua categoria é a \033[1;32mMASTER!!\033[m')
