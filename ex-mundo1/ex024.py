print('\033[1;35m===== EX 024 =====\033[m')

x = str(input('Ponha o nome da sua cidade? '))

y = x.lower()
p = y.split()
j = p[0]  
z = 'santo' in j

print(f'O nome da sua cidade contém a palavra Santo no primeiro nome? {z}')