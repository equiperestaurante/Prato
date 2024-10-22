# Importando a classe Prato
from prato import Prato

# Criando a instância da classe Prato e garantindo que a tabela seja criada
prato_instancia = Prato()

# Menu de opções
while True:
    print("\n <------ Menu do Restaurante ------>")
    print("\n1. Cadastrar prato")
    print("2. Consultar todos os pratos")
    print("3. Consultar prato por ID")
    print("4. Atualizar prato")
    print("5. Deletar prato")
    print("6. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        # Cadastrar prato
        nome = input("Nome do prato: ")
        preco = float(input("Preço do prato: "))
        descricao = input("Descrição do prato: ")
        prato_instancia.cadastrarPrato(nome, preco, descricao)

    elif opcao == 2:
        # Consultar todos os pratos
        print("\nLista de todos os pratos cadastrados:")
        prato_instancia.consultarPratos()

    elif opcao == 3:
        # Consultar um prato pelo ID
        id = int(input("Informe o ID do prato: "))
        prato_instancia.consultarPratoIndividual(id)

    elif opcao == 4:
        # Atualizar os dados de um prato
        id = int(input("Informe o ID do prato a ser atualizado: "))
        nome = input("Novo nome do prato (pressione Enter para não alterar): ")
        preco = input("Novo preço do prato (pressione Enter para não alterar): ")
        preco = float(preco) if preco else None
        descricao = input("Nova descrição do prato (pressione Enter para não alterar): ")
        prato_instancia.atualizarPrato(id, nome if nome else None, preco, descricao if descricao else None)

    elif opcao == 5:
        # Deletar prato pelo ID
        id = int(input("Informe o ID do prato a ser deletado: "))
        prato_instancia.deletarPrato(id)

    elif opcao == 6:
        # Sair do programa
        print("Encerrando o programa...")
        prato_instancia.fechar_conexao()  # Fechar a conexão ao sair
        break

    else:
        print("Opção inválida! Escolha uma opção válida.")

