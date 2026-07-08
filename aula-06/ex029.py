def analisar_financiamento():
    valor_casa = float(input())
    salario = float(input())
    anos = int(input())

    prestacao = valor_casa / (anos * 12)
    limite = salario * 0.30

    if prestacao <= limite:
        print("Empréstimo Concedido")
    else:
        print("Empréstimo Negado")

if __name__ == "__main__":
    analisar_financiamento()