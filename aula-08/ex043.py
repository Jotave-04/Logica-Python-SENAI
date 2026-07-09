import random

computador = random.randint(0, 10)
tentativas = 0

while True:
    palpite = int(input("Digite seu palpite (0 a 10): "))
    tentativas += 1
    
    if palpite == computador:
        break
    elif palpite < computador:
        print("Mais... Tente um número maior.")
    else:
        print("Menos... Tente um número menor.")

print(f"Acertou! Foram necessárias {tentativas} tentativas.")