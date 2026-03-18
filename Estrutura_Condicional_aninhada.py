import os
os.system("cls" if os.name == "nt" else "clear")

# Estrutura Condicional Aninhada
conta_normal = True
conta_premium = False
valor_compra = float(input("Digite o valor da compra: "))   

if conta_normal:
    if valor_compra >= 100:
        print("Compra aprovada")
    else:
        print("Valor mínimo para compra é de R$100,00") 
elif conta_premium:
    if valor_compra >= 50:
        print("Compra aprovada")
    else:
        print("Valor mínimo para compra é de R$50,00")
