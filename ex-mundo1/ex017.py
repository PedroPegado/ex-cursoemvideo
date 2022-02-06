print('\033[1;35m===== EX 017 =====\033[m')
from math import hypot

co = float(input('DIGITE O CATETO OPOSTO = '))
ca = float(input('DIGITE O CATETO ADJACENTE = '))
h1 = hypot(co, ca)

print(f'A HIPOTENUSA É {h1:.2f}')