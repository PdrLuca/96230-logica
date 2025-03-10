import os
os.system("clear")

valor_produto = float(input("Digite o valor do produto: "))
pagamento = input("""Digite o meio de Pagamento:
1- Pagamento á prazo
2- Pagamento á vista               
""")

match pagamento:
    case 1:
        desconto = valor_produto * 0.10
        print("valor do produto")
    case _:
        
        print("Opção Inválida.")

print("==FIM==")

    
