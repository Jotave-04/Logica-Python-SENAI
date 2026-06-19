a = input("Digite algo: ")

print(f"Tipo primitivo: {type(a)}")

print(f"Somente espaços em branco? {a.isspace()}")

print(f"É numérico? {a.isnumeric()}")

print(f"É alfabético? {a.isalpha()}")

print(f"É alfanumérico? {a.isalnum()}")

print(f"Está em MAIÚSCULAS? {a.isupper()}")

print(f"Está em minúsculas? {a.islower()}")

print(f"Está Capitalizado? {a.istitle()}")