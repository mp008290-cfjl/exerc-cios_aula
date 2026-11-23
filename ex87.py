vetor_x = []
vetor_y = []


print("Digite os 8 valores do vetor X:")
for i in range(8):
    valor = int(input(f"X[{i}]: "))
    vetor_x.append(valor)

    print("\nDigite os 8 valores do vetor Y:")
for i in range(8):
    valor = int(input(f"Y[{i}]: "))
    vetor_y.append(valor)

    print("\nResultados das multiplicações:")
for i in range(8):
    resultado = vetor_x[i] * vetor_y[i]
    print(f"X[{i}] × Y[{i}] = {resultado}")