numero = int(input("Digite um número para calcular o fatorial: "))

if numero < 0:
    print("Fatorial não está definido para números negativos.")
else:
    fator = numero
    fatorial = 1
    termos = []
    
    if numero == 0:
        print("0! = 1")
    else:
        while fator > 0:
            termos.append(str(fator))
            fatorial *= fator
            fator -= 1
        
        calculo_visual = " x ".join(termos)
        print(f"{numero}! = {calculo_visual} = {fatorial}")