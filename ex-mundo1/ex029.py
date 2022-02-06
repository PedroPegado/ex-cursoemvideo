print('\033[1;35m===== EX 029 =====\033[m')

velo = int(input('Tá em que velocidade? '))
multa = (velo - 80) * 7

if velo > 80:
    print(f'OPA OPA OPA, passou o limite de 80Km/h permitido, multinha vai chegar em casa tá? {multa:.2f} reais')
else:
    print('Tenha um bom dia! Dirija com segurança e alegria.')
