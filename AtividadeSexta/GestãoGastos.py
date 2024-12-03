# Sistema de Gestão de Orçamento 
receita_total = 0
despesa_total = 0
despesa_alimentacao = 0
despesa_transporte = 0
despesa_lazer = 0
despesa_outras = 0

while True:
    print("\nEscolha uma opção:")
    print("1. Inserir Receita")
    print("2. Inserir Despesa")
    print("3. Mostrar Relatório")
    print("4. Sair")
    
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor_receita = float(input("Digite o valor da receita: "))
        receita_total += valor_receita
        print(f"Receita de R$ {valor_receita:.2f} adicionada com sucesso!")

    elif opcao == "2":
        valor_despesa = float(input("Digite o valor da despesa: "))
        print("Escolha a categoria da despesa:")
        print("1. Alimentação")
        print("2. Transporte")
        print("3. Lazer")
        print("4. Outras")
        
        categoria = input("Digite o número da categoria: ")

        if categoria == "1":
            despesa_alimentacao += valor_despesa
        elif categoria == "2":
            despesa_transporte += valor_despesa
        elif categoria == "3":
            despesa_lazer += valor_despesa
        else:
            despesa_outras += valor_despesa
        
        despesa_total += valor_despesa
        print(f"Despesa de R$ {valor_despesa:.2f} adicionada com sucesso na categoria escolhida.")

    elif opcao == "3":
        print("\n--- Relatório de Orçamento ---")
        print(f"Receita Total: R$ {receita_total:.2f}")
        print(f"Despesa Total: R$ {despesa_total:.2f}")
        print(f"Saldo: R$ {receita_total - despesa_total:.2f}")
        print("\n--- Despesas por Categoria ---")
        print(f"Alimentação: R$ {despesa_alimentacao:.2f}")
        print(f"Transporte: R$ {despesa_transporte:.2f}")
        print(f"Lazer: R$ {despesa_lazer:.2f}")
        print(f"Outras: R$ {despesa_outras:.2f}")

    elif opcao == "4":
        print("Até mais! Não se esqueça de marcar suas despesas.")
        break

    else:
        print("Opção inválida. Tente novamente.")
