soma = 0
quantidade = 0
maior = None
menor = None

while True:
    numero = int(input("Digite um número inteiro: "))
    
    soma += numero
    quantidade += 1
    
    if maior is None or numero > maior:
        maior = numero
    if menor is None or numero < menor:
        menor = numero
        
    resposta = input("Quer continuar? [S/N]: ").strip().upper()
    if resposta == 'N':
        break

if quantidade > 0:
    media = soma / quantidade
    print(f"\nQuantidade de números digitados: {quantidade}")
    print(f"Média entre todos os valores: {media:.2f}")
    print(f"Maior valor lido: {maior}")
    print(f"Menor valor lido: {menor}")