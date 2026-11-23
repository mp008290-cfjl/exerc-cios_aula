print("programa para mostrar os 18 valores que você solicitou")
print()

valores = [0] * 18


for i in range(len(valores)):
    valores[i] = int(input(f"informe o {i + 1}°: "))
    
for i in range(len(valores)):

    print()
    print(f"{valores[i]}")
    print("--------------------")