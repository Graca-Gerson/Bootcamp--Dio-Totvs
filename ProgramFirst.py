import os
print("Bem-vindo ao Python Simples em Python!")
def limpar_tela():
    os.system("cls" if os.name == "nt" else "clear")

## Estrutura condicional simples
def verificar_idade():
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Você é maior de idade.")
    else:
        print("Você é menor de idade.")
        print("Acesso negado.")
        
        