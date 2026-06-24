# CALCULANDO TINTA PARA PINTAR PAREDE

largura = float(input("Largura da parede (m): "))
altura = float(input("Altura da parede (m): "))
area = largura * altura
tinta = area / 2
print(f"\nSua parede: {largura} x {altura} m")
print(f"Área total: {area:.3f} m2")
print(f"Tinta necessária: {tinta:.4f} litros")