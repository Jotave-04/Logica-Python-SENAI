# ALUGUEL DE CARROS

dias = int(input("Dias alugados: "))
km = float(input("Quilômetros rodados: "))
custo_diaria = dias * 60
custo_km = km * 0.15
total = custo_diaria + custo_km
print(f"\nDiárias ({dias} dias): R$ {custo_diaria:.2f}")
print(f"Quilometragem: R$ {custo_km:.2f}")
print(f"TOTAL A PAGAR: R$ {total:.2f}")