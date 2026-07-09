while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    if sexo in ("M", "F"):
        break
    else:
        print("Sexo inválido! Tente novamente")

print("Cadastro realizado com sucesso!")