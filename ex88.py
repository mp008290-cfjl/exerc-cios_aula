alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i + 1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))
