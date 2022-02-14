def notas(*n, sit=False):
    """
    -> FUNÇÕES PARA ANALISAR NOTAS E SITUAÇÕES DE VÁRIOS ALUNOS.
    :param n: Uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não acidinoar a situação
    :return: dicionario com varios informações sobre o desempenho da turma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['situação'] = 'BOA'
        elif r['media'] >= 5:
            r['situação'] = 'RAZOAVEL'
        else:
            r['situação'] = 'UMA MERDA'
    return r


# Programa Princi
resp = notas(5.5, 2.5, 9, 8.5, 10, sit=True)
print(resp)
