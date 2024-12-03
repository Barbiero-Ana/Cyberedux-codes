import random

num = int(input('Digite o número para saber o número secreto!: '))

s_numero = random.randint(0, 10)
placar = 0

while num != s_numero:
    placar += 1
    if num < s_numero:
        print(f'O número secreto é maior que {num}')
    else:
        print(f'O número secreto é menor que {num}')
    num = int(input('Tente novamente: '))



print(f' Você acertou! O número sorteado era: {s_numero}')
print(f' Seu placar de tentativas foi de: {placar}')