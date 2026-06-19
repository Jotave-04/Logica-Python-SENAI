nome = input("Olá, qual seu nome? ")

print(f"Nome digitado: {nome}")

print(f"Tipo primitivo: {type(nome)}")

print(f"Somente espaços em branco? {nome.isspace()}")

print(f"É numérico? {nome.isnumeric()}")

print(f"É alfabético? {nome.isalpha()}")

print(f"É alfanumérico? {nome.isalnum()}")

print(f"Está em MAIÚSCULAS? {nome.isupper()}")

print(f"Está em minúsculas? {nome.islower()}")

print(f"Está Capitalizado? {nome.istitle()}")