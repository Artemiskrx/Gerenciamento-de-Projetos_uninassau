def menu_funcionarios():
    while True:
        print("\n===== MENU DE FUNCIONÁRIOS =====")
        print("1 - Cadastrar funcionário")
        print("2 - Listar funcionários")
        print("3 - Buscar funcionário")
        print("4 - Atualizar funcionário")
        print("5 - Excluir funcionário")
        print("0 - Voltar")

        opcao = input("Escolha uma opção: ")

        try:
            if opcao == "1":
                print("Cadastrar funcionário")

            elif opcao == "2":
                print("Listar funcionários")

            elif opcao == "3":
                print("Buscar funcionário")

            elif opcao == "4":
                print("Atualizar funcionário")

            elif opcao == "5":
                print("Excluir funcionário")

            elif opcao == "0":
                break

            else:
                print("Opção inválida!")

        except Exception as erro:
            print(f"Erro: {erro}")

            