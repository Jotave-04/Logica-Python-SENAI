# Número real entre 0 e 1
from random import random
n = random()
print(f'O número real escolhido entre 0 e 1 foi: {n: .2f}')

# Inteiro entre 1 e 10
from random import randint
n = randint(1, 10)
print(f'O inteiro escolhido foi {n}')

# Escolhe 1 elemento de uma lista
from random import choice
lista= [1, 2, 3, 4, 5, 6, 7, 8, 9]
escolhido = choice(lista)
print(f'O escolhido foi {escolhido}')

# Embaralha uma lista (in-place)
from random import shuffle
lista= [1, 2, 3, 4, 5, 6, 7, 8, 9]
shuffle(lista)
print(f'A lista embaralhada é {lista}')