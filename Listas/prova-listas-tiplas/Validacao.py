'''
3 - Crie uma função validar_idades(lista_idades) que:
- Receba uma lista de idades
- Verifique se todas as idades são válidas (entre 0 e 120)
- Retorne uma lista apenas com idades válidas
- Imprima a quantidade de idades inválidas removidas
- Calcule a média das idades válidas
Exemplo de entrada: [25, 17, 150, 42, -3, 65, 88]
'''

def validar_idades():
    lista_id = []
    qntd = int(input(f'Digite a quantidade de idades que deseja inserir: '))

    for i in range(qntd):
        idade = int(input(f'Digite a {i + 1} idade: '))
        lista_id.append(idade)
    
    idade_valid = [idade for idade in lista_id if 0 <= idade <= 120]
    idade_invalid = len(lista_id) - len(idade_valid)

    media = sum(idade_valid)/ len(idade_valid) if idade_valid else 0 #média das idades válidas

    print(f'\nIdades válidas presentes na listagem: {idade_valid}')
    print(f'\nIdades inválidas removidas da listagem: {idade_invalid}')
    print(f'\nMédia das idades válidas: {media}')

validar_idades()