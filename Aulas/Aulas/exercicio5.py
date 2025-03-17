import os

os.system("cls || clear")

for i in range(3):
    nota = float(input(f"Digite a nota da {i+1}a unidade:"))
    soma += nota
    media = soma / 3

if media >= 7:
    print("Aprovado")
elif media < 4:
    print("Reprovado")

print(f"media: {media}")

print("Inicio do programa")

