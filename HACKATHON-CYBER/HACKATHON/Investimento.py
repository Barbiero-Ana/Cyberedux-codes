import math
from rich.theme import Theme

estilo = Theme({
    'certo': 'bold green',
    'error': 'bold red',
    'titulo': 'bold underline magenta',
    'entrada': 'bold yellow',
    'saida': 'bold cyan'
})

def opcoes():
    print('\nOpções de investimento disponíveis:\n') 
    for chave, (nome, taxa) in investimentos.items():
        print(f'{chave}. {nome} - Rendimento de {taxa}% ao mês')

def calcu_taxa(valor, taxa, meses):
    return valor * (1 + (taxa / 100)) ** meses

def obt_invest():
    while True:
        try:
            opc = int(input('\nEscolha onde deseja investir seus fundos (digite o número correspondente): '))
            if opc in investimentos:
                return opc
            else:
                print('Opção inválida! Escolha um número listado.')
        except ValueError:
            print('Opção inválida! Por favor, digite apenas números!')

def obter_valor():
    while True:
        try:
            valor = float(input('\nDigite o valor que deseja investir: '))
            return valor
        except ValueError:
            print('Valor inválido.')

def tempo():
    while True:
        try:
            meses = int(input('\nDigite quanto tempo você deseja deixar os fundos rendendo (em meses): '))
            return meses
        except ValueError:
            print('Valor inválido! Digite um valor numérico inteiro.')

def menu():
    while True:
        print('Deseja realizar um investimento? sim/não')
        respo = input('\n- ').lower()
        if respo == 'sim':
            opcoes()  
            opc = obt_invest()  
            nome_invest, taxa_rendimento = investimentos[opc]
            valor_init = obter_valor()  
            meses = tempo()  

            vf = calcu_taxa(valor_init, taxa_rendimento, meses)

            print(f'\nVocê escolheu investir em {nome_invest}.')
            print(f'Durante {meses} meses, seu investimento de R${valor_init:.2f} se tornará R${vf:.2f}.')
        else:
            print('Retornando ao menu inicial.')
            break  

        
        novamente = input('\nDeseja realizar outro investimento? sim/não: ').lower()
        if novamente != 'sim':
            print('Retornando ao menu inicial.')
            break
#-------------------------------------------------------------------------------------------------------------------------------
investimentos = {
    1: ('Poupança', 0.5),
    2: ('CDB', 0.8),
    3: ('Fundos imobiliários', 1.2),
    4: ('Tesouro Selic', 0.7),
    5: ('Peer-to-Peer lending', 1.4),
    6: ('Debêntures', 1.0),
    7: ('Fundo multimercado', 1.1)
}

menu()
