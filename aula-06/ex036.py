def pagamento_loja():
    preco_base = float(input())
    print("1 — Dinheiro/Cheque\n2 — Cartão à Vista\n3 — 2x no Cartão\n4 — 3x ou mais")
    opcao = int(input())

    match opcao:
        case 1:
            total = preco_base * 0.90
            print(f"{total:.2f}")
        case 2:
            total = preco_base * 0.95
            print(f"{total:.2f}")
        case 3:
            total = preco_base
            parcela = total / 2
            print(f"{total:.2f} (2x de {parcela:.2f})")
        case 4:
            total = preco_base * 1.20
            parcelas = int(input())
            parcela = total / parcelas
            print(f"{total:.2f} ({parcelas}x de {parcela:.2f})")
        case _:
            print("Opção inválida")

if __name__ == "__main__":
    pagamento_loja()