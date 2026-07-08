def converter_base():
    numero = int(input())
    print("1 - Binário\n2 - Octal\n3 - Hexadecimal")
    opcao = input()

    if opcao == "1":
        print(bin(numero)[2:])
    elif opcao == "2":
        print(oct(numero)[2:])
    elif opcao == "3":
        print(hex(numero)[2:])

if __name__ == "__main__":
    converter_base()