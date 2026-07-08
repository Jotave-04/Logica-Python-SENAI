def gerar_tabuada():
    numero = int(input())

    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

if __name__ == "__main__":
    gerar_tabuada()