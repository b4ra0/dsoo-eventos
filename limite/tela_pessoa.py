class TelaPessoa():
    def tela_opcoes(self):
        print("-------- PESSOAS ----------")
        print("Escolha a opção")
        print("1 - Incluir Pessoa")
        print("2 - Alterar Pessoa")
        print("3 - Listar Pessoa")
        print("4 - Excluir Pessoa")
        print("0 - Retornar")

        opcao = int(input("Escolha a opção: "))
        return opcao

    def pega_dados_pessoa(self):
        print("-------- DADOS PESSOA ----------")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de Nascimento: ")
        endereco = input("Endereço: ")

        return {"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco}

    def mostra_pessoa(self, dados_pessoa):
        print("NOME DA PESSOA: ", dados_pessoa["nome"])
        print("CPF DA PESSOA: ", dados_pessoa["cpf"])
        print("DATA DE NASCIMENTO DA PESSOA: ", dados_pessoa["data_nascimento"])
        print("ENDEREÇO DA PESSOA: ", dados_pessoa["endereco"])
        print("\n")
        
    def seleciona_pessoa(self):
        nome = input("Nome da pessoa que deseja selecionar: ")
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)