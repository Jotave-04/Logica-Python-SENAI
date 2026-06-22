'''
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2

print(f"A soma entre {n1} e {n2} vale {soma}")
'''

def soma(n1, n2):
    resultado = n1 + n2
    return resultado

def principal():
    numero1 = int(input("Digite o 1° número: "))
    numero2 = int(input("Digite o 2° número: "))

    somatorio = soma(numero1, numero2)

    print(f"O somatório é: {somatorio}")

principal()