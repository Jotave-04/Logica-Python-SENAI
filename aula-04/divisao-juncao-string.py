# split() DIVIDIR EM LISTA

frase = 'LÓGICA DE PROGRAMAÇÃO'
partes = frase.split()
print(f'Dividido em partes: {partes}') # Dividido em partes: ['LÓGICA', 'DE', 'PROGRAMAÇÃO']
print(f'Primeira parte: {partes[0]}') # Primeira parte: LÓGICA
print(f'Última parte: {partes[-1]}') # Última parte: PROGRAMAÇÃO
print(f'Total de partes: {len(partes)}') # Total de partes: 3


# join REUNIR UMA LISTA

frase = ['LÓGICA', 'DE', 'PROGRAMAÇÃO']
resultado = '-'.join(frase)
print(f'Usando hífen: {resultado}') # Usando hífen: LÓGICA-DE-PROGRAMAÇÃO

