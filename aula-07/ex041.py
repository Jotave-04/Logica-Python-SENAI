def verificar_maioridade_coletiva():
    maiores = 0

    for _ in range(1, 8):
        ano_nasc = int(input())
        idade = 2026 - ano_nasc
        if idade >= 21:
            maiores += 1

    print(f"{maiores} pessoa(s) atingiram a maioridade de 21 anos")

if __name__ == "__main__":
    verificar_maioridade_coletiva()