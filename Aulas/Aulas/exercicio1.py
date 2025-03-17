import os
import time
os.system("cls || clear")

print("Inicio do programa")

numero = int(input("Digite um numero:"))

for i in range(5,0,-1):
    print(f"{numero} x {i} = {numero * i}")
    time.sleep(0.6)
print("Fim do Programa")                  