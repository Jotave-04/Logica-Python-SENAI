# SORTEANDO ALUNO DE UMA LISTA

import random

n1 = input("Digite o nome do 1° aluno: ")
n2 = input("Digite o nome do 2° aluno: ")
n3 = input("Digite o nome do 3° aluno: ")
n4 = input("Digite o nome do 4° aluno: ")

nomes = [n1, n2, n3, n4]

sorteado = random.choice(nomes)

print(f"A pessoas sorteada para a tarefa foi: {sorteado}")