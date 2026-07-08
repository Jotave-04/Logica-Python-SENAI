def classificar_atleta():
    idade = int(input())

    if idade <= 9:
        print("Mirim")
    elif idade <= 14:
        print("Infantil")
    elif idade <= 19:
        print("Júnior")
    elif idade <= 25:
        print("Sênior")
    else:
        print("Máster")

if __name__ == "__main__":
    classificar_atleta()