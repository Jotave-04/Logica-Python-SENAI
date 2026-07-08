distancia = float(input("Digite a distância da viagem em km: "))

if distancia <= 200:
    tarifa = 0.50
    preco = distancia * tarifa
else:
    tarifa = 0.45
    preco = distancia * tarifa

print(f"Para uma viagem de {distancia:.1f} km, a tarifa aplicada é de R$ {tarifa:.2f} por km.")
print(f"O preço total da passagem é: R$ {preco:.2f}")