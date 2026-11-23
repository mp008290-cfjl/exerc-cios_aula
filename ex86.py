print("programa para contar a quantidade de vezes que o x aparece no vetor")

pessoas = []

for i in range(10):
    numero = int(input(f"Digite o {i + 1}º número inteiro: "))
    numero.append(numero)

x = int(input("Digite o número inteiro X: "))

quantidade = numero.count(x)

print(f"O número {x} aparece {quantidade} vez(es) no vetor.")