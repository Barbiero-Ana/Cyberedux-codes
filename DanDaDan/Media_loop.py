# Peça ao usuário para digitar 5 notas. Use um loop para somar as notas e calcular a média

soma = 0

for i in range (5):
    nota = float(input('Digite as notas: '))
    soma += nota
    
media = soma/5
print(f'A soma das notas será: {soma}')
print(f'A média será: {media}')