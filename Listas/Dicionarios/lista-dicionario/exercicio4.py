'''
4. Crie um dicionário com 5 países como chave e suas capitais como valor. Permita que o usuário 
consulte a capital de um país.

'''

lista = {
    'Brasil' : 'Brasilia',
    'Japão'  :  'Tóquio',
    'França' :  'París',
    'Alemanha' : 'Berlim',
    'Canadá'  : 'Ottawa',

}

verificar = input('Digite o país que deseja verificar: ')

if verificar in lista:
    print(f'A capital do país {verificar} é {lista[verificar]}')
else:
    print('Erro! Não possui.')
