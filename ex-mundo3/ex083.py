valor = str(input('Digite a expressão: '))
pilha = []
for simb in valor:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('VALIDA.')
else:
    print('INVALIDA')