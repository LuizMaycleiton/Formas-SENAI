lista_compras = ["Pão", "Ovo", "Leite", "Carne"]

def mostrar():
    for lista in lista_compras:
        print(f"Sua lista de compras atualmente é:   {lista}")

def cadastro():
    item = input("Escreva o que você quer adicionar na lista: ")
    lista_compras.append (item)

def remover():
    remocao = input("Escreva o que você quer tirar da lista: ")
    lista_compras.remove (remocao)

def modificar():
    antigo = input("Escreva o item que você quer MODIFICAR: ")

    if antigo in lista_compras:
        novo = input(f"Escreva o novo valor para substituir '{antigo}': ")
        posicao = lista_compras.index(antigo)
        lista_compras[posicao] = novo
        print("Item modificado com sucesso!")
    else:
        print(f"Erro: '{antigo}' não foi encontrado na lista.")


    

while True:
    print("Lista de Compras ")
    print("---------------------------------------------")
    print("1 - Mostrar lista ")
    print("2 - Cadastrar item na lista ")
    print("3 - Excluir item na lista ")
    print("4 - Modificar item na lista ")
    print("0 - Sair")
    print("---------------------------------------------")

    opcao = input("Escolha uma opcão: ")

    if opcao == "1":
        mostrar()

    elif opcao == "2":
        cadastro()

    elif opcao == "3":
        remover()

    elif opcao == "4":
        modificar()

    elif opcao == "0":
        print("---------------------------------------------")
        print("Saindo do sistema...")
        break

    else:
        print("---------------------------------------------")
        print("Ação indisponivel...")





