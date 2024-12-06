produtos = []

# Solicit o nome e preço dos items
for i in range(3):  
    nome = input(f"Digite o nome do produto {i+1}: ")
    preco = float(input(f"Digite o preço do {nome}: "))
    produtos.append({"nome": nome, "preco": preco})

# variavel para armazenar o mais caro
produto_mais_caro = produtos[0]

# comparar preço
for produto in produtos[1:]:
    if produto["preco"] > produto_mais_caro["preco"]:
        produto_mais_caro = produto

print("\nProduto mais caro:")
print("Nome:", produto_mais_caro["nome"])
print("Preço:", produto_mais_caro["preco"])
