
# 1. Abre o arquivo para leitura
arquivo = open("roupas.txt", "r", encoding="utf-8")

# 2. Lê todas as linhas
linhas = arquivo.readlines()

# 3. Fecha o arquivo
arquivo.close()

# 4. Mostra todas as roupas
print("=== ROUPAS DA LOJA ===")

for linha in linhas:
    dados = linha.strip().split(",")

    nome = dados[0]
    preco = float(dados[1])

    print(f"Roupa: {nome} - Preço: R$ {preco:.2f}")
