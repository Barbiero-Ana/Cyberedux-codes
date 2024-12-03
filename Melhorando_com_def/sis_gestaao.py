def acesso():
    senha_acesso = 'senha@123'
    tentativa = 3
    while tentativa > 0:
        senha = input('Digite sua senha de acesso: ')
        if senha == senha_acesso:
            print('Acesso liberado.')
            return True
        else:
            print('Acesso negado. Tente novamente')
            tentativa -= 1
    print('Acesso negado.')
    return False

def adicionar_receita(saldo):
    valor = float(input('Digite o valor da receita a ser adicionado: '))
    return saldo + valor

def add_gastos(saldo, alimentacao, lazer, transporte, outros):
    categ = int(input('Digite o tipo de categoria a ser adicionado o gasto\n 1 - alimentação \n 2 - lazer \n 3 - transporte \n 4 - outros \n: '))
    if categ == 1:
        valor = float(input('Digite o valor do gasto: '))
        alimentacao += valor
    elif categ == 2:
        valor = float(input('Digite o valor do gasto: '))
        lazer += valor
    elif categ == 3:
        valor = float(input('Digite o valor do gasto: '))
        transporte += valor
    else:
        valor = float(input('Digite o valor do gasto: '))
        outros += valor
    saldo -= valor
    return saldo, alimentacao, lazer, transporte, outros

def exib_sald(saldo):
    print('\n ================ Resumo financeiro  ================ ')
    print(f'O saldo atual é de: {saldo}')

def dash(alimentacao, lazer, transporte, outros):
    print('\n ================ Dashboard de gastos  ================')
    print(f'O gasto em alimentação foi de: {alimentacao}')
    print(f'O gasto em lazer foi de: {lazer}')
    print(f'O gasto em transporte foi de: {transporte}')
    print(f'O gasto em outras áreas foi de: {outros}')

def gerenciamento():
    saldo = 1000
    alimentacao = lazer = transporte = outros = 0
    while True:
        print('Opções:')
        print('1 - Adicionar receita \n2 - Adicionar despesa \n3 - Exibir saldo \n4 - Exibir dashboard \n5 - Sair')
        op = input('Digite a opção desejada: ')

        if op == '1':
            saldo = adicionar_receita(saldo)  
        elif op == '2':
            saldo, alimentacao, lazer, transporte, outros = add_gastos(saldo, alimentacao, lazer, transporte, outros) 
        elif op == '3':
            exib_sald(saldo) 
        elif op == '4':
            dash(alimentacao, lazer, transporte, outros)  
        elif op == '5':
            print('Até mais!')  
            break 
        else:
            print('Opção inválida. Escolha uma opção válida.')


if acesso():
    gerenciamento()
