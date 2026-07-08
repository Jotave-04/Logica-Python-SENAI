velocidade = float(input("Digite a velocidade atual do veículo (em km/h): "))

if velocidade > 80:
    km_excedente = velocidade - 80
    multa = km_excedente * 7
    
    print(f"ALERTA: Você ultrapassou o limite de 80 km/h!")
    print(f"Condutor MULTADO por excesso de velocidade.")
    print(f"Valor da multa: R$ {multa:.2f}")

if velocidade <= 80:
    print("Velocidade dentro do limite permitido. Boa viagem e dirija com segurança!")