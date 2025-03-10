import os
os.system("clear")

opção = int(input("""
Código \t Prato \t\t Valor
1 \t  \t R$ 25,00
2 \t Lasanha \t R$ 20,00
3 \t Strogonoff \t\t 18,00
4 \t Bife acebolado \t\t 15,00
5 \t Pão com ovo \t\t 5,00

Digite a opção desejada:
"""))

match opção:
    case "1":
        resultado = ("Picanha")
    
    case "2":
        resultado = ("Lasanha")
    
    case "3":
        resultado = ("Sreogonoff")
    
    case "4":
        resultado = ("Bife acebolado")
    
    case "5":
        resultado = ("Pão com ovo")

    case _:
        resultado = "opção inválida."

       
    