opcao_escolhida = ""
while (opcao_escolhida != "0"):
    print ("1 - Mostrar o nome")
    print ("2 - Mostrar o cidade")
    print ("3 - Mostrar o média")
    print ("4 - Mostrar o situação")
    print ("0 - Sair")
    opcao_escolhida = input("Escolha uma das opções: ")
    print ("#"*20)
    if (opcao_escolhida == "1"):
        print ("Fernando Leonid")
    elif (opcao_escolhida  == "2"):
        print ("São Roque")
    elif (opcao_escolhida == "3"):
        print (7)
    elif (opcao_escolhida == "4"):
        print ("Aprovado")
    elif (opcao_escolhida == "0"):
        print ("Saindo do Sistema...")
    else:
        print ("Opção incorreta, tente novamente!")
    print ("#"*20)