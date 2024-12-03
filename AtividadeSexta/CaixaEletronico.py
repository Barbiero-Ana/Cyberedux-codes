
saldo = 1000.00
senha_armazenada = "1234"  


while True:
    # entrad. usuario
    tentativa = input("Digite a senha para acessar sua conta: ")
    
    if tentativa == senha_armazenada:
        print("Senha correta! Bem-vindo ao Caixa Eletrônico.")
        
        # Menu de op
        while True:
            print("\nEscolha a operação desejada:")
            print("1 - Consultar saldo")
            print("2 - Depositar dinheiro")
            print("3 - Sacar dinheiro")
            print("4 - Sair")
            
            opcao = input("Digite a opção desejada (1-4): ")
            
            if opcao == "1":
                print(f"Seu saldo atual é: R$ {saldo:.2f}")
            
            elif opcao == "2":
                valor = float(input("Digite o valor a ser depositado: R$ "))
                if valor > 0:
                    saldo += valor
                    print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
                else:
                    print("Valor inválido para depósito.")
            
            elif opcao == "3":
                valor = float(input("Digite o valor a ser sacado: R$ "))
                if valor > 0 and valor <= saldo:
                    saldo -= valor
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
                elif valor > saldo:
                    print("Saldo insuficiente!")
                else:
                    print("Valor inválido para saque.")
            
            elif opcao == "4":
                print("Saindo... Obrigado por usar o Caixa Eletrônico!")
                break
            
            else:
                print("Opção inválida! Tente novamente.")
            
            # saida da operação
            continuar = input("Deseja realizar outra operação? (s/n): ").lower()
            if continuar != 's':
                print("Saindo... Obrigado por usar o Caixa Eletrônico!")
                break
        if continuar != 's':
            break
    else:
        print("Senha incorreta! Tente novamente.")
