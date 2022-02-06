print('\033[1;35m===== EX 022 =====\033[m')

nome = str(input('Digite seu nome completo: '))

up = (nome.upper())
lw = (nome.lower())
nom = nome.strip()
qc = (len(nom) - nome.count(' '))
nom2 = nome.split()
qc1 = (len(nom2[0])) #podia ser tbm nome.find(' '), para achar quantas letras tem o primeiro nome.

print(f'Só com letras maiúsculas: {up}\nSó com letras minúsculas: {lw}\nQuantidade de caracteres: {qc}\nQuantidade de caracteres no primeiro nome: {qc1}')