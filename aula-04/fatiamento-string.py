frase = "Lógica de Programação"
frase[0] # 'L' → caractere na posição 0
frase[10] # 'P' → décimo primeiro caractere (índice começa em 0)
frase[10:20] # 'PROGRAMAÇÃ' → do 10 até o 19 (20 excluído)
frase[10:] # 'PROGRAMAÇÃO' → do 10 até o final
frase[:6] # 'LÓGICA' → do início até o 5 (6 excluído)
frase[::3] # a cada 3 caracteres → 'LI OAÇ'
frase[10:20:3] # a cada 3 caracteres → 'PGMÃ'

# =========================================================================

frase = 'LÓGICA DE PROGRAMAÇÃO'
print(f'No índice 0 temos o caracter: {frase[0]}')
print(f'No índice 10 temos o caracter: {frase[10]}')
print(f'Do índice 10 até 20 temos os caracteres: {frase[10:20]}')
print(f'Do índice 10 em diante temos os caracteres: {frase[10:]}')
print(f'Do primeiro índice até o 6 temos os caracteres: {frase[:6]}')
print(f'Do primeiro índice ao último, pulando de 3 em 3: {frase[::3]}')
print(f'Do índice 10 até o 20, pulando de 3 em 3: {frase[10:20:3]}')