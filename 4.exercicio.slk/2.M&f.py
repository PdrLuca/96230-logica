import os
os.system("clear")

sexo = input("Digite seu sexo:").lowwer()
altura = int(input("Digite sua altura:"))

match sexo:
    case "M":
        peso_ideal = (72.7*altura)-58
        print(f"\nPeso ideal: {peso_ideal}")
    case "F":
        peso_ideal = (62.1*altura)-44.7
        print(f"\nPeso ideal: {peso_ideal}")
    case _:
        print("opção inválida")