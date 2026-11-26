x = int(input("Digite o número inteiro X: "))
numeros = []

for i in range(32):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

    quantidade = numeros.count(x)

print(f"\nO número {x} apareceu {quantidade} vez(es).")