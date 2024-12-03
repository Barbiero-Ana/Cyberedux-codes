aluno = {'nome': 'pedro', 'idade': 22}

dicionario = {}

print(aluno['nome'])

aluno.get('curso', 'não encontrado')

aluno['curso'] = 'matemática'
aluno['nome'] = 'João'

#dessa forma eu removo do dicionário
#aluno.pop('idade')

for chave, valor in aluno.items():
    print(f'{chave}: {valor}')