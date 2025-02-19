# Limpar o terminal.
import os
os.system("clear")

primeiro_numero = float(input("Digite a primeira nota: "))
segundo_numero = float(input("Digite a segunda nota: "))

soma = primeiro_numero + segundo_numero
media = soma/2

produto = primeiro_numero * segundo_numero

if primeiro_numero < segundo_numero:
    menor = primeiro_numero
    maior = segundo_numero
else:
    menor = segundo_numero
    maior = primeiro_numero


print("\nexibindo resultados: ")
print(f"media: {media}")
print(f"produto: {produto}")
print(f"menor: {menor}")
print(f"maior: {maior}")
