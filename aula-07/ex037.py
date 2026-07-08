from time import sleep

def contagem_regressiva_deploy():
    for i in range(10, -1, -1):
        print(i)
        sleep(1)
    print("Deploy concluído com sucesso! 🎆")

if __name__ == "__main__":
    contagem_regressiva_deploy()