def area(lado):
    resultado = lado ** 2
    return resultado

def principal():
    n1 = int(input("Digite em cm o tamanho do lado do quadrado: "))
    area_total = print(f"A área do quadrado é {area(n1)}")
    return area_total
principal()