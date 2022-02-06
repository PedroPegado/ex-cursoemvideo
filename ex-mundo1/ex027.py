print('\033[1;35m===== EX 027 =====\033[m')

x = input('Escreva seu nome completo: ')

y = x.upper()
z = y.split()
f1 = z[0]
f2 = y.split()
f3 = f2[-1]

print(f'Seu primeiro nome é: {f1}')
print(f'Seu ultimo nome é: {f3}')