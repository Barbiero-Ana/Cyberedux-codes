'''
1 - Crie um dicionário onde a chave seja o nome do aluno e o valor seja sua nota. Adicione 3 alunos 3 calcule a média das notas
'''

aluno = {'lucas': 10.5, 'Albert': 2.5, 'Juliana': 10.0}

total = sum(aluno.values())

media = total / len(aluno)

print(f'A média dos alunos será: {media:.2f}')