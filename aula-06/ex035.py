def calcular_imc():
    peso = float(input())
    altura = float(input())

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print("Abaixo do peso")
    elif imc < 25.0:
        print("Peso ideal")
    elif imc < 30.0:
        print("Sobrepeso")
    elif imc < 40.0:
        print("Obesidade")
    else:
        print("Obesidade Mórbida")

if __name__ == "__main__":
    calcular_imc()