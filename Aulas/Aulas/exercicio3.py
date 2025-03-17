import os

os.system("cls || clear")

print("Inicio do programa")
soma = 0
for i in range(5):
    nota = float(input(f"Digite o {i+1}o numéro: "))
    soma = soma + nota

print(f"soma: {soma}")

print("Fim do Programa")