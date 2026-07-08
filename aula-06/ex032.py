from datetime import datetime

def verificar_alistamento():
    nascimento = int(input())
    ano_atual = datetime.now().year
    idade = ano_atual - nascimento

    if idade == 18:
        print("Aliste-se imediatamente")
    elif idade < 18:
        faltam = 18 - idade
        print(f"Faltam {faltam} anos")
    else:
        passou = idade - 18
        print(f"Prazo vencido há {passou} anos")

if __name__ == "__main__":
    verificar_alistamento()