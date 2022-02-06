from limite.tela_abstrata import TelaAbstrata

class TelaPessoa(TelaAbstrata):

    def tela_opcoes(self):
        print("-------- PESSOAS ----------")
        print("Escolha a opção")
        print("1 - Adicionar Pessoa")
        print("2 - Alterar Pessoa")
        print("3 - Listar Pessoa")
        print("4 - Excluir Pessoa")
        print("0 - Retornar")

        opcao = self.le_num_inteiro("Escolha uma opção: ", [1, 2, 3, 4, 0])
        return opcao

    def le_num_inteiro(self, mensagem: str = "", inteiros_validos=None):
        return super().le_num_inteiro(mensagem, inteiros_validos)

    def pega_dados_pessoa(self):
        print("-------- DADOS PESSOA ----------")
        tipo = input("Tipo da pessoa (1 - Participante, 2 - Organizador): ")
        nome = input("Nome: ")
        cpf = input("CPF: ")
        data_nascimento = input("Data de Nascimento: ")
        endereco = input("Endereço: ")
        vacina = input("Vacina (0: False - 1: True): ")

        return {"tipo": tipo, "nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, 
                "endereco": endereco, "vacina": vacina}

    def mostra_pessoa(self, dados_pessoa):
        print("NOME DA PESSOA: ", dados_pessoa["nome"])
        print("CPF DA PESSOA: ", dados_pessoa["cpf"])
        print("DATA DE NASCIMENTO DA PESSOA: ", dados_pessoa["data_nascimento"])
        print("ENDEREÇO DA PESSOA: ", dados_pessoa["endereco"])
        print("SITUAÇÃO DE VACINA: ", dados_pessoa["vacina"])
        print("\n")
        
    def seleciona_pessoa(self):
        nome = input("Nome da pessoa que deseja selecionar: ")
        return nome
    
    def mostra_mensagem(self, msg):
        print(msg)
