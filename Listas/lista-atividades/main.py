import gerenciador

def sis_gerenciador():

    tarefas = []

    while True:
        gerenciador.menu()
        opcao = input('Digite a opção que deseja: ')
        if opcao == '1':
            gerenciador.add_tarefas(tarefas)
        elif opcao == '2':
            gerenciador.concluido(tarefas)
        elif opcao == '3':
            gerenciador.lista(tarefas)
        elif opcao == '4':
            print('\nSaindo do sistema.\n')
            break
        else:
            print('Opção inválida!')

sis_gerenciador()