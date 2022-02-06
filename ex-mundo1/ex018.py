print('\033[1;35m===== EX 018 =====\033[m')
from math import *

num = float(input('Escolha um ângulo: '))

cos = cos(radians(num))
seno = sin(radians(num))
tan = tan(radians(num))

print(f'O seno de {num} é {seno:.2f}')
print(f'O cosseno de {num} é {cos:.2f}')
print(f'A tangente de {num} é {tan:.2f}')