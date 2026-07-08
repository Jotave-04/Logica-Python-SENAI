def status_aluno():
    nota1 = float(input())
    nota2 = float(input())
    
    media = (nota1 + nota2) / 2

    if media < 5.0:
        print("Reprovado")
    elif media < 7.0:
        print("Recuperação")
    else:
        print("Aprovado")

if __name__ == "__main__":
    status_aluno()