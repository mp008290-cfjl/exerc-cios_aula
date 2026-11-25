alunos = []

print("programa que mostra a nota média dos alunos e os nomes dos alunos com nota inferior a de 7")
print()

for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))

media = sum(nota for nome, nota in alunos) / len(alunos)


print(f"\nMédia das notas: {media:.2f}")
print("Alunos com nota menor que 7:")

for nome, nota in alunos:
    if nota < 7:
        print(nome)