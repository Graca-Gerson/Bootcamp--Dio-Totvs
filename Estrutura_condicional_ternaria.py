import os
os.system("cls" if os.name == "nt" else "clear")

# Estrutura Condicional - Ternária
idade = int(input("Digite sua idade: "))
situacao = "Menor de idade" if idade < 18 else "Adulto" if idade < 65 else "Idoso"
print(f"Você é: {situacao}")
