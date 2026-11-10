
# Sistema de cadastro de roupas

def adicionar_roupa():
    arquivo = open("roupas.txt", "a", encoding="utf-8")

    nome = input("Digite o nome da roupa: ")
    preco = input("Digite o preço da roupa: ")

    arquivo.write(nome + "," + preco + "\n")
    arquivo.close()

    print("Roupa adicionada com sucesso!")


def tirar_roupa():
    try:
        with open("roupas.txt", "r", encoding="utf-8") as arquivo:
            roupas = arquivo.readlines()
    except FileNotFoundError:
        print("Não existem roupas cadastradas.")
        return

    nome = input("Digite o nome da roupa que deseja tirar: ")

    removida = False
    novas_roupas = []

    for roupa in roupas:
        dados = roupa.strip().rsplit(",", 1)

        if dados[0].lower() == nome.lower() and not removida:
            removida = True
        else:
            novas_roupas.append(roupa)

    with open("roupas.txt", "w", encoding="utf-8") as arquivo:
        arquivo.writelines(novas_roupas)

    if removida:
        print("Roupa retirada com sucesso!")
    else:
        print("Roupa não encontrada!")


def listar_roupas():
    try:
        with open("roupas.txt", "r", encoding="utf-8") as arquivo:
            roupas = arquivo.readlines()

        print("\n--- ROUPAS CADASTRADAS ---")

        if not roupas:
            print("Nenhuma roupa cadastrada.")
        else:
            for roupa in roupas:
                print(roupa.strip())

    except FileNotFoundError:
        print("Nenhuma roupa cadastrada.")


# Menu principal
while True:
    print("\n===== LOJA DE ROUPAS =====")
    print("1 - Adicionar roupa")
    print("2 - Tirar roupa")
    print("3 - Ver roupas cadastradas")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_roupa()

    elif opcao == "2":
        tirar_roupa()

    elif opcao == "3":
        listar_roupas()

    elif opcao == "4":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")
