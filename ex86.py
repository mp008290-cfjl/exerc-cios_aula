pessoas = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numeros.append(numero)

x = int(input("Digite o número inteiro X: "))

quantidade = numeros.count(x)

print(f"O número {x} aparece {quantidade} vez(es) no vetor.")