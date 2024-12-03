'''
2. Crie um perfil de um usuário de um site ou rede social (você define quais atributos o perfil terá)
'''

from datetime import datetime



perfil = {}

while True:
    nome = input("Digite seu nome (ou 's' para sair): ")
    if nome.lower() == 's':
        break

    print('\nFeminino\nMasculino\nPrefiro Não dizer\n')
    genero = ''
    while genero.lower() not in ['feminino', 'masculino', 'prefiro não dizer']:
        genero = input('Digite seu gênero: ')
        if genero.lower() not in ['feminino', 'masculino', 'prefiro não dizer']:
            print('Inválido! Tente novamente.')

    
    idade = input('Digite sua idade: ')

    while not idade.isdigit():
        print('Inválido! Tente novamente.')
        idade = input('Digite sua idade: ')
    idade = int(idade)

    print('\nDigite sua data no formato (DD/MM/AAAA)\n')
    birth = input('Digite sua data de aniversário: ')
    try:
        birth_format = datetime.strptime(birth, "%d/%m/%Y")
    except ValueError:
        print("\nFormato de data inválido. Tente novamente.")
        continue
    print('\nAdicione uma bio ao seu perfil!\n')
    bio = input('\n- ')

    break

perfil[nome] = {

    'Nome'   : nome,
    'Gênero' : genero,
    'Idade'  : idade,
    'Data de nascimento'  : birth,
    'Biografia'  : bio,
}

print(f'\nSalvando as alterações..\n')
print(f'\nPerfil salvo!\n')

for chave, valor in perfil[nome].items():
    print(f'\n{chave}: {valor}\n')
