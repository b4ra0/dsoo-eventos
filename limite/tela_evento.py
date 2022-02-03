class TelaEvento():

    def __init__(self, controlador_evento):
        self.__controlador_evento = controlador_evento


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
                "local": local, "capacidade_max": capacidade_max, "organizador": organizadores}

    def mostra_evento(self, dados_evento):
        print("TÍTULO DO EVENTO: ", dados_evento["titulo"] )
        print("DATA DO EVENTO: ", dados_evento["data"])
        print("LOCAL DO EVENTO: ", dados_evento["local"])
        print("CAPACIDADE MÁXIMA DO EVENTO: ", dados_evento["capacidade_max"])
        print("ORGANIZADORES DO EVENTO: ", dados_evento["organizador"])
        #print("PARTICIPANTES DO EVENTO: ", dados_evento["participantes"])
        print("\n")

    def seleciona_evento(self):
        titulo = input("Título do evento que deseja selecionar: ")
        return titulo

    def mostra_ranking(self, ranking, dados_evento):
        print("RANKING DE EVENTOS POR PARTICIPANTES")
        print(ranking, dados_evento["titulo"])


    def mostra_mensagem(self, msg):
        print(msg)