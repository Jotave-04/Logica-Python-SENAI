import math # Import módulo

num = int(input("Digite um número: "))
raiz = math.sqrt(num)

print(f"A raiz de {num} é igual a {raiz:.2f}")

# =================================================

from math import sqrt # Import apenas da função sqrt (raiz quadrada)

num = int(input("Digite um número: "))
raiz = sqrt(num)

print(f"A raiz de {num} é igual a {raiz:.2f}")