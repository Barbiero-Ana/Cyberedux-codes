import validacao

cpf = (input('Digite seu CPF: '))
if validacao.validar_cpf(cpf):
    print('\nCPF válido!\n')
else:
    print('\nCPF inválido.\n')

email = input('Digite seu email: ')
if validacao.validar_email(email):
    print('\nEmail válido!\n')
else:
    print('\nEmail inválido\n')


print('\nDigite o DDD com ()\n')

telefone = (input('\nDigite seu número de telefone: '))
if validacao.validar_telefone(telefone):
    print('\nTelefone válido!\n')
else: 
    print('\nTelefone inválido\n')

print('\nSua senha deve conter: 1 caracter especial, 1 letra maiuscula, 1 letra minuscula e 1 número.\n')
senha = input('Digite sua senha: ')
if validacao.validar_senha(senha):
    print('\nSenha válida!\n')
else:
    print('\nSenha inválida.\n')
