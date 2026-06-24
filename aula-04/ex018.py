# MÉTODO 1 - math

from math import trunc

num = float(input("Digite um número: "))

inteiro = trunc(num)

print(f"O valor digitado foi {num} e sua porção inteira é {inteiro}")

# MÉTODO 2 - int() nativo

num = float(input("Digite um valor: "))

inteiro = int(num)

print(f"O valor digitado é {num} sua porção inteira é {inteiro}")