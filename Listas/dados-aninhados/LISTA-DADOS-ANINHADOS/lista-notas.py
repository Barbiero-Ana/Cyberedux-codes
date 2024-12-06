alunos = [
    {"nome": "Carlos", "notas": [6.0, 7.0, 8.0]},
    {"nome": "Lucia", "notas": [9.0, 8.5, 10.0]},
    {"nome": "Pedro", "notas": [5.0, 4.5, 6.0]}
]


alunos_acima_de_7 = []

for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    if media > 7.0:
        alunos_acima_de_7.append(aluno["nome"])


print("Alunos com média maior que 7.0:")
if alunos_acima_de_7:
    for nome in alunos_acima_de_7:
        print(f"- {nome}")
else:
    print("Nenhum aluno com média maior que 7.0.")
