import math

print("Bem-vindo à Calculadora")
print("Digite '0' para encerrar o programa.")

while True:
    operacao = input('Digite a opção desejada! \n 1: + \n 2: - \n 3: * \n 4: / \n 5: raiz quadrada \n 6: potenciação \n 7: Seno \n 8: Cosseno \n 9: Tangente \n 10: Log \n digite sua opção desejada:')
    
    if operacao == "0":
        print("Encerrando a calculadora.")
        break
    
    if operacao in ["1", "2", "3", "4"]:
        x = float(input("Digite o primeiro número: "))
        y = float(input("Digite o segundo número: "))

        if operacao == "1":
            print('soma')
            resultado = x + y
        elif operacao == "2":
            print('subtração')
            resultado = x - y
        elif operacao == "3":
            print('multiplicação')
            resultado = x * y
        elif operacao == "4":
            print('divisão')
            if y == 0:
                resultado = "Erro: Divisão por zero"
            else:
                resultado = x / y
    
    elif operacao == "5":
        print('raiz quadrada')
        x = float(input("Digite o número: "))
        resultado = math.sqrt(x)
    
    elif operacao == "6":
        print('potenciação')
        x = float(input("Digite a base: "))
        y = float(input("Digite o expoente: "))
        resultado = math.pow(x, y) 
    
    elif operacao == "7":
        print('Seno')
        x = float(input("Digite o ângulo em graus: "))
        resultado = math.sin(math.radians(x))
    
    elif operacao == "8":
        print('Cosseno')
        x = float(input("Digite o ângulo em graus: "))
        resultado = math.cos(math.radians(x))
    
    elif operacao == "9":
        print('Tangente')
        x = float(input("Digite o ângulo em graus: "))
        resultado = math.tan(math.radians(x))
    
    elif operacao == "10":
        print('log')
        x = float(input("Digite o número: "))
        resultado = math.log(x)
    
    else:
        print("Operação inválida. Tente novamente.")
        continue

    print(f"Resultado: {resultado}\n")
