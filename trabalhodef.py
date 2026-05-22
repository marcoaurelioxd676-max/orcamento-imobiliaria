import csv

print("===== IMOBILIÁRIA R.M =====")

# Escolha do imóvel
tipo = input("Digite o tipo do imóvel (apartamento/casa/estudio): ").lower()

valor = 0

# APARTAMENTO
if tipo == "apartamento":

    quartos = int(input("Quantos quartos? "))
    garagem = input("Deseja garagem? (s/n): ").lower()
    criancas = input("Possui crianças? (s/n): ").lower()

    valor = 700

    if quartos == 2:
        valor += 200

    if garagem == "s":
        valor += 300

    # desconto de 5%
    if criancas == "n":
        valor = valor - (valor * 0.05)

# CASA
elif tipo == "casa":

    quartos = int(input("Quantos quartos? "))
    garagem = input("Deseja garagem? (s/n): ").lower()

    valor = 900

    if quartos == 2:
        valor += 250

    if garagem == "s":
        valor += 300

# ESTUDIO
elif tipo == "estudio":

    vagas = int(input("Quantidade de vagas: "))

    valor = 1200

    if vagas >= 2:

        valor += 250

        vagas_extras = vagas - 2

        if vagas_extras > 0:
            valor += vagas_extras * 60

# Tipo inválido
else:
    print("Tipo de imóvel inválido!")
    exit()

# Contrato
valor_contrato = 2000
parcelas = valor_contrato / 5

# Resultado
print("\n===== ORÇAMENTO =====")
print(f"Valor do aluguel: R$ {valor:.2f}")
print(f"Valor do contrato: R$ {valor_contrato:.2f}")
print(f"Contrato parcelado em 5x de R$ {parcelas:.2f}")

# Gerar CSV
arquivo = open("orcamento.csv", "w", newline="", encoding="utf-8")

escritor = csv.writer(arquivo)

escritor.writerow(["Mes", "Valor do aluguel"])

for i in range(1, 13):
    escritor.writerow([i, valor])

arquivo.close()

print("\nArquivo CSV gerado com sucesso!")
