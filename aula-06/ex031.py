def comparar_numeros():
    num1 = int(input())
    num2 = int(input())

    if num1 > num2:
        print("Primeiro maior")
    elif num2 > num1:
        print("Segundo maior")
    else:
        print("Iguais")

if __name__ == "__main__":
    comparar_numeros()