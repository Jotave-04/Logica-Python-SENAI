def main():
    total_compra = 0.0

    while True:
        print('\n=== Menu do Caixa ===')
        print('1 - Adicionar produto')
        print('2 - Finalizar compra')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            try:
                valor = float(input('Digite o valor do produto (R$): '))
            except ValueError:
                print('Valor inválido. Digite um número.')
                continue

            if valor < 0:
                print('Valor do produto não pode ser negativo.')
                continue

            total_compra += valor
            print(f'Produto adicionado: R$ {valor:.2f}')
            print(f'Total parcial: R$ {total_compra:.2f}')

        elif opcao == '2':
            print('\nFinalizando compra...')
            break

        else:
            print('Opção inválida. Tente novamente.')

    if total_compra == 0:
        print('Nenhum produto foi adicionado.')
        return

    if total_compra > 100:
        desconto = total_compra * 0.10
        valor_final = total_compra - desconto
        print(f'Compra acima de R$ 100,00. Desconto de 10% aplicado: R$ {desconto:.2f}')
    else:
        desconto = 0.0
        valor_final = total_compra
        print('Compra abaixo de R$ 100,00. Nenhum desconto aplicado.')

    print(f'Total da compra: R$ {total_compra:.2f}')
    print(f'Valor final a pagar: R$ {valor_final:.2f}')


main()