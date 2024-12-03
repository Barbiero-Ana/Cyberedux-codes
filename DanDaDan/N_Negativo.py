
n_negativo =[]

for i in range (4):
    numero = int(input('Digite um número:  '))

    if numero < 0:
        n_negativo.append(numero)

if n_negativo:
    print('O números negativos são: ')
    for numero in n_negativo:
        print(numero)

else:
    print('Nenhum número negativo foi apresentado.')