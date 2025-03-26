import random

def jogar():
    print("Bem-vindo ao jogo de Adivinhação!")
    
    # Gerar um número aleatório entre 1 e 100
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    acerto = False

    while not acerto:
        # Solicitar ao jogador que insira um palpite
        try:
            palpite = int(input("Digite um número entre 1 e 100: "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        # Contabilizar as tentativas
        tentativas += 1

        # Verificar se o palpite está correto
        if palpite < numero_secreto:
            print("O número é maior! Tente novamente.")
        elif palpite > numero_secreto:
            print("O número é menor! Tente novamente.")
        else:
            acerto = True
            print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
            jogar_novamente()

def jogar_novamente():
    resposta = input("Gostaria de jogar novamente? (s/n): ").strip().lower()
    if resposta == 's':
        jogar()
    else:
        print("Obrigado por jogar!")

# Iniciar o jogo
jogar()
