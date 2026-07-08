numero = int(input("Digite um número inteiro qualquer: "))

verde = "\033[32m"
amarelo = "\033[33m"
reset = "\033[m"

if numero % 2 == 0:
    print(f"O número {numero} é {verde}PAR{reset}!")
else:
    print(f"O número {numero} é {amarelo}ÍMPAR{reset}!")