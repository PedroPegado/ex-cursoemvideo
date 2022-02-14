x = input('digite uma palavra: ').strip().upper().replace(' ', '')
if x == x[::-1]:
    print('palindromo')
else:
    print('nao palindromo')

#frase = input('digite uma palavra: ').strip().upper()
#palavras = frase.split()
#junto = ''.join(palavra)
#inverso = ''
#for letra in range(len(junto)-1, -1, -1)
    #inverso += junto[letra]
#if inverso == junto:
    #print('temos um palindromo')
#else:
    #print('nao é um palindromo')

