print("programa para ler o nome e a idade e listar as pessoas com mais de 18 anos")

QTDE = 7
nomes = [""] * QTDE
idades = [0] * QTDE

for i in range(QTDE):
    nomes[i] = str(input(f"informe o nome da pessoa {i + 1}: "))
    idades[i] = int(input(f"informe a idade da pessoa {i + 1}: "))
    print()

print("pessoas maiores de idade")
for i in range(QTDE):
    if idades[i] >= 18:
        print(f"-{nomes[i]}")
    