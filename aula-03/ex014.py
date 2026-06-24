# CALCULANDO DESCONTO

preco = float(input("R$ Preço do produto: "))
desconto = preco * 5 / 100
novo_preco = preco - desconto
print(f"\nPreço original: R$ {preco:.2f}")
print(f"Desconto (5%): R$ {desconto:.2f}")
print(f"Preço final: R$ {novo_preco:.2f}")