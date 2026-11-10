
# 1. Abre o arquivo para leitura
arquivo = open("roupas.txt", "r", encoding="utf-8")
linhas = arquivo.readlines()
arquivo.close()

# 2. Inicializa as variáveis
maior_preco = 0
roupa_mais_cara = ""

# 3. Percorre todas as linhas
for linha in linhas:
    dados = linha.strip().split(",")

    nome = dados[0]
    preco = float(dados[1])

    # 4. Compara os preços
    if preco > maior_preco:
        maior_preco = preco
        roupa_mais_cara = nome

# 5. Exibe o resultado
print(f"Roupa mais cara: {roupa_mais_cara} com R$ {maior_preco:.2f}")
