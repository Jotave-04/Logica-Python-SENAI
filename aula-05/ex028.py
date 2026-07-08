print("--- Analisador de Triângulos ---")

r1 = float(input("Digite o comprimento da primeira reta (R1): "))
r2 = float(input("Digite o comprimento da segunda reta (R2): "))
r3 = float(input("Digite o comprimento da terceira reta (R3): "))

if (r1 < r2 + r3) and (r2 < r1 + r3) and (r3 < r1 + r2):
    print("\n\033[32mOs segmentos ACIMA PODEM FORMAR um triângulo!\033[m")
else:
    print("\n\033[31mOs segmentos ACIMA NÃO PODEM FORMAR um triângulo!\033[m")