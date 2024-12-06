alunos = []

num_alunos = int(input("Quantos alunos você deseja adicionar? "))

for i in range(num_alunos):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    notas = []
    for j in range(3):  # Vamos pedir 3 notas para cada aluno
        nota = float(input(f"Digite a nota {j+1} de {nome}: "))
        notas.append(nota)
    
    alunos.append({"nome": nome, "notas": notas})


alunos_acima_de_7 = []

for aluno in alunos:
    media = sum(aluno["notas"]) / len(aluno["notas"])
    if media > 7.0:
        alunos_acima_de_7.append({"nome": aluno["nome"], "notas": aluno["notas"], "média": media})


print("\nAlunos com média maior que 7.0:")
if alunos_acima_de_7:
    for aluno in alunos_acima_de_7:
        print(f"- {aluno['nome']}: Notas = {aluno['notas']}, Média = {aluno['média']:.2f}")
else:
    print("Nenhum aluno com média maior que 7.0.")
