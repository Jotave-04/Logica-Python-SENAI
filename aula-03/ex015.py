# REAJUSTE SALARIAL

salario = float(input("R$ Salário atual: "))
aumento = salario * 15 / 100
novo_salario = salario + aumento
print(f"\nSalário anterior: R$ {salario:.2f}")
print(f"Aumento (15%): R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")