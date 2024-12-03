import re
from datetime import datetime

# Buscar entender melhor como funciona a validação do CPF - busquei no chat
def validar_cpf(cpf):

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
    

def validar_email(email):
    if '@' in email and '.' in email.split('@')[-1]:
        return True
    return False

def validar_telefone(telefone):
    
    telefone = telefone.replace('(', '').replace(')', '').replace('-', '').replace('','')
    if len(telefone) in [10, 11] and telefone.isdigit():
        return True
    return False

def validar_data(data):
    try:
        dia, mes, ano = data.split('/')
        datetime(int(ano)), int(mes), int(dia)
        return True
    except:
        return False

def validar_senha(senha):
    maiuscula = False
    minuscula = False
    numero = False
    char_especial = False

    for char in senha:
        if char.isupper():
            maiuscula = True
        elif char.islower():
            minuscula = True
        elif char.isdigit():
            numero = True
        elif char in '!@#$%¨&*(),.[]{}><:"':
            char_especial = True
    if len(senha) >= 5 and maiuscula and minuscula and numero and char_especial:
        return True
    return False