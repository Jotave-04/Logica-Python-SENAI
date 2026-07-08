salario_anterior = float(input("Digite o salário atual do funcionário: R$ "))

if salario_anterior <= 1250.00:
    porcentagem = 15
    novo_salario = salario_anterior + (salario_anterior * 15 / 100)
else:
    porcentagem = 10
    novo_salario = salario_anterior + (salario_anterior * 10 / 100)

print("\n--- Resumo do Reajuste Salarial ---")
print(f"Salário anterior: R$ {salario_anterior:.2f}")
print(f"Percentual de aumento aplicado: {porcentagem}%")
print(f"Novo salário com reajuste: R$ {novo_salario:.2f}")