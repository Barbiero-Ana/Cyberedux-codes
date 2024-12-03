import calculadora

def menu():
    print('Seja bem vindo(a) a calculadora de terminal! \nsegue abaixo a lista de opções disponiveis para uso:')
    print('Caso deseje sair da calculadora digite 0')
    print('\n 1 - Adição \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 5 - Seno \n 6 - Cosseno \n 7 - Tangente \n 8 - Logaritimo \n 9 -Raíz Quadrada ')

def executar(opc):
    if opc in [1, 2, 3, 4]:
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        if opc == 1:
            print(f'\nA soma dos dois números será: {calculadora.adicao(num1, num2)}\n')
        elif opc == 2:
            print(f'\nA subtração dos dois números será: {calculadora.subtracao(num1, num2)}\n')
        elif opc == 3:
            print(f'\nA multiplicação dos dois números será de: {calculadora.multiplicacao(num1, num2)}\n')
        elif opc == 4:
            print(f'\nA divisão dos dois números será de: {calculadora.divisao(num1, num2)}\n')
    elif opc in [5, 6, 7, 8, 9]:
        num = float(input('Digite o número que deseja: '))
        if num == 5:
            print(f'\nO seno do número será: {calculadora.seno(num)}\n')
        elif num == 6:
            print(f'\nO cosseno do número será: {calculadora.cosseno(num)}\n')
        elif num == 7:
            print(f'\nA tangente do número será: {calculadora.tangente(num)}\n')
        elif num == 8:
            print(f'\nO log do número será: {calculadora.log(num)}\n')
        elif num == 9:
            print(f'\nA raíz quadrada do número será: {calculadora.raiz(num)}\n')
        else:
            print('Comando inválido, erro!')
    elif opc == 0:
        print('Até mais!')

while True:
    menu()
    opcao = int(input('Digite a opção desejada: '))
    if opcao == 0:
        print('Até mais!')
        break
    executar(opcao)