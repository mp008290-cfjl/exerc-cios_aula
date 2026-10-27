print("programa para mostrar os 11 valores que você solicitou")
print()

valores = [0] * 11

for i in range(len(valores)):
    valores[i] = float(input("informe um numero: "))
    print("--------------------")
    