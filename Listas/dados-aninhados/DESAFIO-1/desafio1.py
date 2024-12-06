
estoque = {}

#  add produto
def adicionar_produto():
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade do produto: "))
    preco = float(input("Digite o preço do produto: "))
    
    if nome in estoque:
        print("Produto já existe. Atualizando informações...")
        estoque[nome]["quantidade"] += quantidade
    else:
        estoque[nome] = {"quantidade": quantidade, "preco": preco}
    
    print(f"Produto '{nome}' adicionado com sucesso.")

# listar produtos
def listar_produtos():
    if not estoque:
        print("O estoque está vazio.")
        return
    
    print("\nLista de produtos em estoque:")
    for nome, dados in estoque.items():
        print(f"Nome: {nome}, Quantidade: {dados['quantidade']}, Preço: R${dados['preco']:.2f}")

#  remover produto
def remover_produto():
    nome = input("Digite o nome do produto a ser removido: ")
    
    if nome in estoque:
        del estoque[nome]
        print(f"Produto '{nome}' removido com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

#  atualizar quantidade
def atualizar_quantidade():
    nome = input("Digite o nome do produto: ")
    
    if nome in estoque:
        quantidade = int(input(f"Digite a nova quantidade de {nome}: "))
        estoque[nome]["quantidade"] = quantidade
        print(f"Quantidade do produto '{nome}' atualizada com sucesso.")
    else:
        print(f"Produto '{nome}' não encontrado no estoque.")

# consultar valor total
def consultar_valor_total():
    total = sum(dados['quantidade'] * dados['preco'] for dados in estoque.values())
    print(f"Valor total em estoque: R${total:.2f}")

# menu
def menu():
    while True:
        print("\nEscolha uma opção:")
        print("1. Adicionar produto")
        print("2. Listar produtos")
        print("3. Remover produto")
        print("4. Atualizar quantidade")
        print("5. Consultar valor total em estoque")
        print("6. Sair")
        
        opcao = input("Digite o número da opção: ")
        
        if opcao == '1':
            adicionar_produto()
        elif opcao == '2':
            listar_produtos()
        elif opcao == '3':
            remover_produto()
        elif opcao == '4':
            atualizar_quantidade()
        elif opcao == '5':
            consultar_valor_total()
        elif opcao == '6':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

menu()
