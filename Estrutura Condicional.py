import os
os.system("cls" if os.name == "nt" else "clear")

# Estrutura Condicional - if, elif, else

idade = int(input("Digite sua idade: "))
    
if idade < 18:
    print("Você é menor de idade.")
elif 18 <= idade < 65:
    print("Você é adulto.")
else:
     print("Você é idoso.")
     print("Acesso liberado.")
     
opcao = int(input("Informe uma opcao: [1] Sacar dinheiro [2] Depositar dinheiro [3] Sair: "))
     
if opcao == 1:
    print("Você escolheu sacar dinheiro.")
elif opcao == 2:
    print("Você escolheu depositar dinheiro.")
elif opcao == 3:
    print("Você escolheu sair.")
else:
    print("Opção inválida.")
    print("Por favor, escolha uma opção válida.")
    
    