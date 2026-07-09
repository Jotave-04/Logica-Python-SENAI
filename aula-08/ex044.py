n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

opcao = 0
while opcao != 5:
    print("\n--- MENU ---")
    print("1 — Somar")
    print("2 — Multiplicar")
    print("3 — Mostrar o maior valor")
    print("4 — Digitar novos números")
    print("5 — Sair do programa")
    
    opcao = int(input("Escolha uma opção: "))
    
    if opcao == 1:
        print(f"Resultado da soma: {n1 + n2}")
    elif opcao == 2:
        print(f"Resultado da multiplicação: {n1 * n2}")
    elif opcao == 3:
        if n1 > n2:
            print(f"O maior valor é: {n1}")
        elif n2 > n1:
            print(f"O maior valor é: {n2}")
        else:
            print("Os dois números são iguais.")
    elif opcao == 4:
        n1 = float(input("Digite o novo primeiro número: "))
        n2 = float(input("Digite o novo segundo número: "))
    elif opcao == 5:
        print("Saindo do programa...")
    else:
        print("Opção inválida. Tente novamente.")