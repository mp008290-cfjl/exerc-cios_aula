numeros = []

print("programa para listar e enumerar a quantidade de números pares e ímpares")

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

soma_impares = 0
multiplicacao_pares = 1



for posicao, numero in enumerate(numeros, start=1):
    if posicao % 2 == 1:
        soma_impares += numero
    else:
        multiplicacao_pares *= numero

print(f"\nSoma dos valores nas posições ímpares: {soma_impares}")
print(f"Multiplicação dos valores nas posições pares: {multiplicacao_pares}")