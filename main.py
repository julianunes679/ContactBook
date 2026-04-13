def contact_menu(agenda):

    while True:
        print("\nMenu de Opções:")
        print("1 - salvar contato")
        print("2 - Editar contato")
        print("3 - Deletar contato")
        print("4 - Favoritar contato")
        print("5 - Desfavoritar contato")
        print("6 - Sair")

        option = input("Escolha uma opção: ")

        if option == "1":
            print("adicionar novo contato")

        elif option == "2":
            print ("Editar contato")
        
        elif option == "3":
            print("Deletar contato")

        elif option == "4":
            print("Marcar contato como favorito")

        elif option == "5":
            print("Desmarcar contato como favorito")

        elif option == "6":
            print("Menu encerrado")
            break

        else:
            print("Opção inválida, tente novamente")