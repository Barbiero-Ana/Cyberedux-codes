
contatos = {
    "João": {"telefone": "1234", "email": "joao@example.com"},
    "Ana": {"telefone": "9876", "email": "ana@example.com"}
}
# Atualizando o número de telefone de Ana
contatos["Ana"]["telefone"] = "7890"


# Impressão personalizada e formatada
print("Agenda de Contatos:\n")
for nome, info in contatos.items():
    print(f"Nome: {nome}")
    print(f"  Telefone: {info['telefone']}")
    print(f"  Email: {info['email']}\n")