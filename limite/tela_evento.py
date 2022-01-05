

class TelaEvento():

    def tela_opcoes(self):

        print("-------- EVENTOS --------")
        print("")
        print("1 - Adicionar evento")
        print("2 - Remover evento")
        print("3 - Alterar evento")
        print("4 - Detalhe evento")
        print("5 - Listar eventos")
        print("6 - Ranking eventos")
        print("0 - Retornar")

        opcao = int(input("Escolha uma opção: "))
        return opcao

    def pega_dados_evento(self):
        print("-------- DADOS EVENTO --------")
        titulo = input("Título do evento: ")
        data = input("Data do evento: ")
        horario_inicio = input("Horário de início do evento: ")
        local = input("Local do evento: ")
        capacidade_max = input("Capacidade máxima do evento: ")
        organizadores = input("Organizadores do evento: ")

        return {"titulo": titulo, "data": data, "horario_inicio": horario_inicio, 
                "local": local, capacidade_max: capacidade_max, organizadores: organizadores}

    def mostra_evento(self):
        print("TÍTULO DO EVENTO: ", )
        print("DATA DO EVENTO: ", )
        print("LOCAL DO EVENTO: ", )
        print("CAPACIDADE MÁXIMA DO EVENTO: ", )
        print("ORGANIZADORES DO EVENTO: ", )
        print("PARTICIPANTES DO EVENTO: ", )

    def seleciona_evento(self):
        nome_evento = input("Título do evento que deseja selecionar: ")
        return nome_evento

    def mostra_mensagem(self, msg):
        print(msg)