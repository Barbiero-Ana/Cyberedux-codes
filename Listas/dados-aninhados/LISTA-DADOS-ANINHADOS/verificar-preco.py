produtos = [
    {"nome": "Notebook", "preco": 3000},
    {"nome": "Celular", "preco": 1500},
    {"nome": "Tablet", "preco": 2000}
]

produto_mais_caro = produtos[0]

for produto in produtos[1:]:
    if produto["preco"] > produto_mais_caro["preco"]:
        produto_mais_caro = produto
        
# Imprimir o nome e preço do produto mais caro
for chave, valor in produto_mais_caro.items():
    print(f'{chave}: {valor}')

print("\nProduto mais caro:", produto_mais_caro["nome"])
print("Preço:", produto_mais_caro["preco"])
