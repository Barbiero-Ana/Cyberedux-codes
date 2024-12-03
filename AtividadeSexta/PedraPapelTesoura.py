import random

vitorias = 0
derrotas = 0
empates = 0

while True:
    print("\nJogo Pedra, Papel e Tesoura")
    print("Escolha uma opção:")
    print("1 - Pedra")
    print("2 - Papel")
    print("3 - Tesoura")
    

    escolha_usuario = int(input("Digite sua escolha (1, 2, 3): "))
    
    if escolha_usuario not in [1, 2, 3]:
        print("Escolha inválida! Tente novamente.")
        continue
    
    # O computador escolhe aleatoriamente
    escolha_computador = random.randint(1, 3)
    
    # respos. comp.
    if escolha_computador == 1:
        escolha_computador_str = "Pedra"
    elif escolha_computador == 2:
        escolha_computador_str = "Papel"
    else:
        escolha_computador_str = "Tesoura"
    
    print(f"O computador escolheu: {escolha_computador_str}")
    
    # sist. de empate
    if escolha_usuario == escolha_computador:
        resultado = "Empate"
        empates += 1
    elif (escolha_usuario == 1 and escolha_computador == 3) or \
        (escolha_usuario == 2 and escolha_computador == 1) or \
        (escolha_usuario == 3 and escolha_computador == 2):
        resultado = "Vitória"
        vitorias += 1
    else:
        resultado = "Derrota"
        derrotas += 1
    
    # result
    print(f"Resultado: {resultado}")
    
    # pontos
    print(f"\nPlacar atual: Vitórias = {vitorias}, Derrotas = {derrotas}, Empates = {empates}")
    
    # recomc
    jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("Obrigado por jogar! Até a próxima.")
        break
