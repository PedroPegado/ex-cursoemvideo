print('\033[1;35m===== EX 025 =====\033[m')

x = input('Ponha seu nome completo: ')

y = x.lower()
z = 'silva' in y

print(f'Seu nome contém o sobrenome Silva? {z}')