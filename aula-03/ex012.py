# CONVERSOR DE MOEDAS

import time

def conversor1():
    brl = float(input("\nQuantos Reais deseja converter? "))
    usd = 5.17
    time.sleep(1)
    resultado = brl / usd
    texto = f"\nNa cotação atual, R${brl:.2f} equivale a ${resultado:.2f}"
    print("\033[4m" + texto + "\033[0m")
    time.sleep(1)

def conversor2():
    usd = float(input("\nQuantos Dólares deseja converter? "))
    brl = 0.19
    time.sleep(1)
    resultado = usd / brl
    texto = f"\nNa cotação atual, ${usd:.2f} equivale a R${resultado:.2f}"
    print("\033[4m" + texto + "\033[0m")
    time.sleep(1)

print("=" * 45)
print("Bem-vindo ao conversor de moedas FIRJAN SENAI")
print("=" * 45)
time.sleep(1)

while True:
    op = input("\nAgora me diga qual operação você deseja executar:\n1. Converter BRL para USD\n2. Converter USD para BRL\n3. Consultar cotação\n4. Sair\nSelecione uma opção: ")    
    time.sleep(1)
    if op == "1": 
        conversor1()
    elif op == "2":
        conversor2()
    elif op == "3":
        print("\nA cotação do dólar hoje é: R$5,17")
        time.sleep(1)
    elif op == "4":
        print("\nObrigado por usar o conversor! Até logo.")
        time.sleep(1)
        break
    else:
        print("\nOperação inválida! Tente novamente")
        time.sleep(1)