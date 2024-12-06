import pprint


contatos = {
    "João": {"telefone": "1234", "email": "joao@example.com"},
    "Ana": {"telefone": "5678", "email": "ana@example.com"}
}

# Função para exibir a agenda de contatos de forma organizada
def exibir_agenda(contatos):
    print("Agenda de Contatos:\n")
    for nome, info in contatos.items():
        print(f"Nome: {nome}")
        print(f"  Telefone: {info['telefone']}")
        print(f"  Email: {info['email']}\n")


print("Agenda original:")
exibir_agenda(contatos)

# Solicitar que o usuário altere o número de telefone de um contato
nome_contato = input("Digite o nome do contato para atualizar o telefone: ")

# Verif de contato existente
if nome_contato in contatos:
    novo_telefone = input(f"Digite o novo número de telefone para {nome_contato}: ")
    contatos[nome_contato]["telefone"] = novo_telefone
    print(f"\nNúmero de telefone de {nome_contato} atualizado com sucesso!")
else:
    print(f"\nContato {nome_contato} não encontrado.")


print("\nAgenda de Contatos Atualizada:")
exibir_agenda(contatos)
