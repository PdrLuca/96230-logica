import os
os.system("clear")


nome = input("Digite seu nome:")
primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota: "))

media = (primeira_nota + segunda_nota/2)

if media >= 9:
  conceito - "A"  
  
elif media > 7.5:
    conceito - "B"

elif media >= 6:
   conceito - "C"

elif media > 4:
   conceito - "D"

else:
   conceito - "E"


match conceito:
    case "A" | "B" | "C":
        print(f"conceito: {conceito}")
        print("Aprovado.")
    case "D" | "E":
        print(f"conceito: {conceito}")
        print("Reprovado.")

    case _:
         print("Opção inválida.")