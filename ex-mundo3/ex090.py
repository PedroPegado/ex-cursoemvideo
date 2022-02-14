alunos = {'aluno':str(input('Digite o nome do aluno: ')),'media':float(input(f'Média do aluno: '))}
print(f'Nome: {alunos["aluno"]}.')
print(f'Média: {alunos["media"]}.')
if alunos['media'] > 7:
    print(f'O aluno {alunos["aluno"]} foi aprovado.')
else:
    print(f'O aluno {alunos["aluno"]} foi reprovado.')

#PODERIA TER USADO O for k, v in alunos.items() PARA MOSTRAR OS VALORES:
#print(f' - {k} é igual a {v}.')


