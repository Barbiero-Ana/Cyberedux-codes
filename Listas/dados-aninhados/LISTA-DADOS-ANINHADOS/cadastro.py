import re

def validar_cpf(cpf):
#VALIDAÇÃO CPF E JESUS AMADO
    cpf = ''.join([c for c in cpf if c.isdigit()])

    if len(cpf) != 11:
        return False

    # Verificar se o CPF é uma sequência repetitiva
    if cpf == cpf[0] * 11:
        return False

    # Cálculo do primeiro dígito verificador
    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    # Pesos para o cálculo do primeiro e segundo dígito
    pesos_primeiro = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    pesos_segundo = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]

    # Cálculo dos dígitos verificadores
    primeiro_digito = calcular_digito(cpf, pesos_primeiro)
    segundo_digito = calcular_digito(cpf, pesos_segundo)

    # Verificar se os dígitos calculados são iguais aos fornecidos
    if int(cpf[9]) == primeiro_digito and int(cpf[10]) == segundo_digito:
        return True
    else:
        return False
#----------------------------------------------------------------------------------------------------------------------------------------
def validar_cep(cep):
    #Validação de CEP
    return bool(re.fullmatch(r'\d{8}', cep))
#----------------------------------------------------------------------------------------------------------------------------------------

def cadastrar_pessoa():
    #colet dados
    print("\n--- Cadastro de Pessoa ---")
    nome = input("Digite o nome completo: ")
    
    cpf = input("Digite o CPF (com os pontos e traços): ")
    while not validar_cpf(cpf):
        print("CPF inválido! Tente novamente.")
        cpf = input("Digite o CPF (com os pontos e traços): ")
    
    data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
    sexo = input("Digite o sexo (Masculino/Feminino): ")
    estado_civil = input("Digite o estado civil (Solteiro, Casado, etc.): ")
    renda_mensal = input("Digite a renda mensal: ")
    
    print("\n--- Endereço ---")
    logradouro = input("Digite o logradouro: ")
    numero = input("Digite o número: ")
    complemento = input("Digite o complemento: ")
    cidade = input("Digite a cidade: ")
    estado = input("Digite o estado: ")
    
    cep = input("Digite o CEP (apenas números): ")
    while not validar_cep(cep):
        print("CEP inválido! Tente novamente.")
        cep = input("Digite o CEP (apenas números): ")
    
    return {
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "sexo": sexo,
        "estado_civil": estado_civil,
        "renda_mensal": renda_mensal,
        "endereco": {
            "logradouro": logradouro,
            "numero": numero,
            "complemento": complemento,
            "cidade": cidade,
            "estado": estado,
            "cep": cep,
        }
    }
#----------------------------------------------------------------------------------------------------------------------------------------

def exibir_cadastros(cadastros):
    #exiber os cadastrossssssss
    print("\n--- Cadastros Realizados ---")
    for i, pessoa in enumerate(cadastros, 1):
        print(f"\nPessoa {i}:")
        for chave, valor in pessoa.items():
            if chave == "endereco":
                print("Endereço:")
                for key, val in valor.items():
                    print(f"{key.capitalize()}: {val}")
            else:
                print(f"{chave.capitalize()}: {valor}")
#----------------------------------------------------------------------------------------------------------------------------------------

def iniciar_cadastro():
    
    cadastros = []
    while True:
        pessoa = cadastrar_pessoa()
        cadastros.append(pessoa)
        print("\nCadastro realizado com sucesso!")
        
        continuar = input("Deseja cadastrar outra pessoa? (S/N): ").strip().lower()
        if continuar != 's':
            break
    exibir_cadastros(cadastros)
