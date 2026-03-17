def calculadora():
    while True:
        print("\n" + "="*20)
        print("  MINHA CALCULADORA")
        print("="*20)
        print("1. Soma (+)")
        print("2. Subtração (-)")
        print("3. Multiplicação (*)")
        print("4. Divisão (/)")
        print("s. Sair")
        
        opcao = input("\nEscolha uma operação: ").lower()

        if opcao == 's':
            print("Até logo! Encerrando...")
            break
        
        if opcao not in ['1', '2', '3', '4']:
            print("❌ Erro: Opção inválida. Tente novamente.")
            continue

        # Validação de Entrada Numérica
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
        except ValueError:
            print("❌ Erro: Por favor, digite apenas números válidos.")
            continue

        # Processamento das Operações
        if opcao == '1':
            resultado = num1 + num2
            print(f"✅ Resultado: {num1} + {num2} = {resultado}")
        
        elif opcao == '2':
            resultado = num1 - num2
            print(f"✅ Resultado: {num1} - {num2} = {resultado}")
        
        elif opcao == '3':
            resultado = num1 * num2
            print(f"✅ Resultado: {num1} * {num2} = {resultado}")
        
        elif opcao == '4':
            # Validação específica para divisão por zero
            if num2 == 0:
                print("❌ Erro: Divisão por zero não é permitida!")
            else:
                resultado = num1 / num2
                print(f"✅ Resultado: {num1} / {num2} = {resultado}")

# Executa o programa
calculadora()