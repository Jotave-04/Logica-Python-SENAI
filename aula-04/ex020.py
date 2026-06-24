# SENO, COSSENO E TANGENTE

from math import radians, sin, cos, tan

angulo = float(input("Digite o ângulo (graus): "))
radiano = radians(angulo)

seno = sin(radiano)
cosseno = cos(radiano)
tangente = tan(radiano)

print(f"O ângulo de {angulo}° tem:")
print(f" Seno: {seno:.2f} | Cosseno: {cosseno:.2f} | Tangente: {tangente:.2f}")