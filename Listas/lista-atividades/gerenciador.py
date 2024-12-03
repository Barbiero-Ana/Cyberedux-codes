'''
Crie um programa que permita ao usuário:
● Adicionar tarefas a uma lista
● Marcar tarefas como concluídas (removendo-as da lista)
● Listar todas as tarefas pendentes 
● Desafio extra: Adicionar prioridade às tarefas

'''

def menu():
    print('\nSeja bem vindo(a) Sistema de Gestão!\n Selecione a opção que atende sua necessidade.\n')
    print('1 - Adicionar uma nova tarefa\n2 - Marcar uma tarefa como concluida\n3 - Listar tarefas pendentes\n4 - Sair\n')

def add_tarefas(tarefas):

    sobre = input('Digite uma descrição ou detalhe da tarefa: ')
    prioridade = input('Digite a prioridade desta tarefa\n1 - Alta\n2 - Média\n3 - Baixa\n:')

    while prioridade not in ['1', '2', '3']:
        print('Dado inválido! Tente novamente.')
        prioridade = input('Digite a prioridade desta tarefa\n1 - Alta\n2 - Média\n3 - Baixa')
    tarefas.append({'Descrição':sobre, 'Prioridade':prioridade})
    print(f'Tarefa adicionada: {sobre} [prioridade: {prioridade}]')

def lista(tarefas):
    if not tarefas:
        print('Nenhuma tarefa pendente.')
        return
    print('\nTarefas pendentes\n')
    prioridades = {'Alta':1, 'Média':2, 'Baixa':3 }
    tarefas_list = sorted(tarefas, key=lambda x: prioridades[x['Prioridade']])
    for i, tarefa in enumerate(tarefas_list, 1):
        print(f'{i}. {tarefa["Descrição"]} [Prioridade: {tarefa["Prioridade"]}]')


def concluido(tarefas):
    lista(tarefas)
    if not tarefas:
        return
    try:
        num = int(input('Digite o número da tarefa concluida: '))
        if 1 <= num <= len(tarefas):
            concluido = tarefas.pop(num - 1)
            print(f'Tarefa concluída e removida: {concluido["Descrição"]}')

        else:
            print('Número inválido.')
    except ValueError:
        print('Entrada inválida! Por favor, insira um número')