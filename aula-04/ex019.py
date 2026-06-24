# CALCULANDO HIPOTENUSA

# UTILIZANDO MÓDULO

import math

cateto1 = int(input("Digite a medida do cateto oposto: "))
cateto2 = int(input("Digite a medida do cateto adjacente: "))

hipotenusa = math.hypot(cateto1,cateto2)

print(f"A hipotenusa do triângulo retângulo com medidas {cateto1} e {cateto2} é {hipotenusa:.2f}")

# FAZENDO A CONTA SEM MÓDULO

cateto1 = int(input("Digite a medida do cateto oposto: "))
cateto2 = int(input("Digite a medida do cateto adjacente: "))

hipotenusa = (cateto1 ** 2 + cateto2 ** 2) ** (1/2)

print(f"A hipotenusa do triângulo retângulo com medidas {cateto1} e {cateto2} é {hipotenusa:.2f}")
