# CONVERSOR DE MEDIDA

medida = float(input("Digite a medida em METROS: "))

km = medida / 1000 # Quilômetro
hm = medida / 100 # Hectômetro
dam = medida / 10 # Decâmetro
dm = medida * 10 # Decímetro
cm = medida * 100 # Centímetro
mm = medida * 1000 # Milímetro

print(f"A conversão de {medida}m para quilômetro é: {km:.5f}km")
print(f"A conversão de {medida}m para hectômetro é: {hm:.4f}hm")
print(f"A conversão de {medida}m para decâmetro é: {dam:.3f}dam")
print(f"A conversão de {medida}m para decímetro é: {dm:.1f}dm")
print(f"A conversão de {medida}m para centímetro é: {cm:.1f}cm")
print(f"A conversão de {medida}m para milímetro é: {mm:.1f}mm")