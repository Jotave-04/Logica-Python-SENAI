"""
n1 = int(input("Digite um número para consulta: "))

dobro = n1 * 2
triplo = n1 * 3
quadruplo = n1 * 4
quintuplo = n1 * 5

print(f"O dobro de {n1} é {dobro}\nO triplo de {n1} é {triplo}\nO quadruplo de {n1} é {triplo}\nO quadruplo de {n1} é {quadruplo}\nO quintuplo de {n1} é {quintuplo}")
"""

def mult(n1):
    for i in range(2, 6):
        resultado = print(f"{n1} X {i} = {n1 * i}")
    return resultado

def principal():
    numero1 = int(input("Digite um valor para saber sua tabuada: "))
    multiplos = mult(numero1)
    return multiplos
principal()
