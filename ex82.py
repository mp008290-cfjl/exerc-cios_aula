print("programa para mostrar os 11 valores que você solicitou")
print()

valores = [0] * 11

for i in range(len(valores)):
    valores[i] = int(input(f"informe o {i + 1}°: "))
    
for i in range(len(valores)):

    print()
    print(f"{valores[i]}")
    print("--------------------")