# CONVERSOR DE MOEDAS

def conversor1(brl,usd):
    brl = int(input("Quantos Reais deseja converter? "))
    usd = 5.17

    conversao = print(f"Na cotação atual, R${brl} sai como ${brl / usd}")
    return conversao

def conversor2(brl,usd):
    brl = int(input("Quantos Dólares deseja converter? "))
    brl = 0.19

    conversao = print(f"Na cotação atual, R${brl} sai como ${usd / brl}")
    return conversao

print("=" * 25)
print("Bem-vindo ao conversor de moedas FIRJAN SENAI")
print("=" * 25)

while True:
    op = input("\nAgora me diga qual operação você deseja executar:\n1. Converter BRL para USD\n2. Converter USD para BRL\n3. Consultar cotação\n4. Sair\nSelecione uma opção: ")    
    if op == "1": 
        conversor1()
    elif op == "2":
        conversor2()
    elif op == "3":
        print("\nA cotação do dólar hoje é: R$5,17")
        print("\nA cotação do real hoje é: $0,19")
    elif op == "4":
        break
    else:
        print("\nOperação inválida! Tente novamente")