from random import randint

numero_sorteado = randint(0, 5)

print("Tente adivinhar o número que eu pensei entre 0 e 5!")

tentativa = int(input("Digite o seu palpite: "))

verde = "\033[32m"
vermelho = "\033[31m"
reset = "\033[m"

if tentativa == numero_sorteado:
    print(f"{verde}PARABÉNS! Você venceu! O número era {numero_sorteado}.{reset}")
else:
    print(f"{vermelho}Você perdeu! O computador venceu. O número pensado era {numero_sorteado}.{reset}")