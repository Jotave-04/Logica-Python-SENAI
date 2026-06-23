# TABUADA FORMATADA

def tabuada(numero):
    for i in range(1,11):
        resultado = print(f"{numero:>3} X {i} = {numero * i}")
        print("=" * 14)
    return resultado



print("=" * 33)
print("Bem-vindo a tabuada FIRJAN SENAI")
print("=" * 33)

numero = int(input("Digite um valor para consultar sua tabuada: "))

tabuada(numero)