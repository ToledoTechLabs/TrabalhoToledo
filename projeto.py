import random

# Função que gera o número aleatório
def jogar_adivinhacao():
    numero_secreto = random.randint(1, 100)
    tentativas_restantes = 5  # Limite de tentativas
    print("Bem-vindo ao Jogo da Adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")
    print(f"Você tem {tentativas_restantes} tentativas para acertar o número.")

    while tentativas_restantes > 0:
        try:
            palpite = int(input(f"\nVocê tem {tentativas_restantes} tentativas restantes. Qual é o seu palpite? "))
        except ValueError:
            print("Por favor, insira um número válido.")
            continue

        if palpite < numero_secreto:
            print("O número é maior. Tente novamente!")
        elif palpite > numero_secreto:
            print("O número é menor. Tente novamente!")
        else:
            print(f"Parabéns! Você acertou o número {numero_secreto}!")
            break

        tentativas_restantes -= 1

    if tentativas_restantes == 0:
        print(f"\nVocê não conseguiu adivinhar o número. O número secreto era {numero_secreto}. Melhor sorte na próxima!")

# Chama a função para jogar
if __name__ == "__main__":
    jogar_adivinhacao()
