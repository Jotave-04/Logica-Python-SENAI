# TRANSFORMANDO STRING

frase = 'LÓGICA DE PROGRAMAÇÃO'
print(f' Letras Maiúsculas: {frase.upper()}') # "LÓGICA DE PROGRAMAÇÃO

print(f' Letras Minúsculas: {frase.lower()}') # "lógica de programação"

print(f' Primeira letra maiúscula: {frase.capitalize()}') # "Lógica de programaç

print(f' Todas as primeiras letras maiúscula: {frase.title()}') # "Lógica De ProgramaçÃO


# ====================================================================================================================

frase = ' LÓGICA DE PROGRAMAÇÃO '

print(f' Frase sem espaços: {frase.strip()}') # "LÓGICA DE PROGRAMAÇÃO

print(f' Frase sem espaços na esquerda: {frase.lstrip()}') # "LÓGICA DE PROGRAMAÇÃO " Retira espaços da esquerda

print(F' Frase sem espaços na direita: {frase.rstrip()}') # " LÓGICA DE PROGRAMAÇÃO" Retira espaços da direita


# =====================================================================================================================

frase = 'LÓGICA DE PROGRAMAÇÃO'

frase_nova = frase.replace('PROGRAMAÇÃO', 'PYTHON')

print(f' Frase alterada: {frase_nova}') # 'LÓGICA DE PYTHON' Substituição de palavras