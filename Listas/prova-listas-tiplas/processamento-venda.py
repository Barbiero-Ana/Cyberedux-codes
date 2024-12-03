'''
2 - Desenvolva um programa que processe uma lista de vendas e:
- Some o total de vendas
- Calcule quantas vendas superaram a média
- Identifique o maior valor de venda
- Crie uma nova lista apenas com vendas acima de R$ 1000,00
Exemplo de entrada: [850.50, 1250.75, 650.25, 1500.00, 980.30]

'''

def process_venda():
    vendas = []
    qunt = int(input('Digite a quantidade de vendas que deseja informar: '))

    for i in range(qunt):
        venda = float(input(f'Digite o valor da {i + 1} venda: \n'))
        vendas.append(venda)
    
    total_vend = sum(vendas)
    media = total_vend / len(vendas)

    up_media = [venda for venda in vendas if venda >  media] #filtrar vendas acima de média
    vendas_1000 = [venda for venda in vendas if venda > 1000] #Filtra as vendas acima de 1000
    maior = max(vendas)
    print('========================================RESUMO===================================================================')
    print(f'\nO total de vendas: {total_vend}\n')
    print(f'\nVendas acima da média: {up_media}\n')
    print(f'\nVendas acimda de R$ 1000,00 : {vendas_1000}\n')
    print(f'\nMaior venda: {maior}\n')

process_venda()