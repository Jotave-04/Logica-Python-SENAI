def analisar_metricas():
    soma = 0
    contador = 0

    for numero in range(1, 501):
        if numero % 2 != 0 and numero % 3 == 0:
            soma += numero
            contador += 1

    print(f"Quantidade: {contador}")
    print(f"Soma: {soma}")

if __name__ == "__main__":
    analisar_metricas()