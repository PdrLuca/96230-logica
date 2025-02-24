import os
os.system("clear")

primeiro_numero=float(input("Digite o primeiro numero: "))
segundo_numero=float(input("Digite o segundo numero: "))

if primeiro_numero > segundo_numero:
    maior= primeiro_numero
    menor= segundo_numero
else: 
    maior= segundo_numero
    menor= primeiro_numero

print("maior:", (maior))
print("menor:", (menor))