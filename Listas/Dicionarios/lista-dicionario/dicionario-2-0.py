'''
1 - Crie um dicionário onde a chave seja o nome do aluno e o valor seja sua nota. Adicione 3 alunos 3 calcule a média das notas 
'''

alunos = {}

for i in range(3):
    nome = input('Digite o nome do aluno: ')
    nota = float(input('Digite a nota do aluno: '))
    alunos[nome] = nota

soma = 0

for nota in alunos.values():
    soma += nota

media = soma / len(alunos)

print(alunos)
print(f'\nA média dos alunos: {media:.2f}\n')