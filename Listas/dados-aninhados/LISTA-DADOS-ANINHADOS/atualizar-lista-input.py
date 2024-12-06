import pprint


contatos = {
    "João": {"telefone": "1234", "email": "joao@example.com"},
    "Ana": {"telefone": "5678", "email": "ana@example.com"}
}

#exibe a lista organizadada
def exibir_agenda(contatos):
    print("Agenda de Contatos:\n")
    for nome, info in contatos.items():
        print(f"Nome: {nome}")
        print(f"  Telefone: {info['telefone']}")
        print(f"  Email: {info['email']}\n")

# Exibindo a agenda antes da atualização
print("Agenda original:")
exibir_agenda(contatos)


nome_contato = input("Digite o nome do contato para atualizar o telefone ou o email: ")

# Verif de contato existente
if nome_contato in contatos:
    opcao = input("O que você deseja atualizar? (1) Telefone (2) Email: ")
    
    if opcao == "1":
        novo_telefone = input(f"Digite o novo número de telefone para {nome_contato}: ")
        contatos[nome_contato]["telefone"] = novo_telefone
        print(f"\nNúmero de telefone de {nome_contato} atualizado com sucesso!")
    elif opcao == "2":
        novo_email = input(f"Digite o novo email para {nome_contato}: ")
        contatos[nome_contato]["email"] = novo_email
        print(f"\nEmail de {nome_contato} atualizado com sucesso!")
    else:
        print("\nOpção inválida!")
else:
    print(f"\nContato {nome_contato} não encontrado.")


print("\nAgenda de Contatos Atualizada:")
exibir_agenda(contatos)
