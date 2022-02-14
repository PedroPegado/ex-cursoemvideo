soma = 0
contagem = 0

for impar in range(1, 501, 2):
        if impar % 3 == 0:
                soma = soma + impar
                contagem = contagem + 1
print(f'\033[1;32mExistem {contagem} numeros multiplos de 3 e a soma deles é {soma}\033[m')
