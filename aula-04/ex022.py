# ANALISADOR DE NOMES COMPLETOS

nome = input("Olá, informe seu nome completo: ").strip()

print(f"Em MAIÚSCULAS: {nome.upper()}")
print(f"Em minúsculas: {nome.lower()}")

total_letras = len(nome) - nome.count(" ")

print(f"Total de letras (sem espaços): {total_letras}")

partes = nome.split()
primeiro = partes[0]

print(f"Seu primeiro nome é '{primeiro}' e tem {len(primeiro)} letras")
