from limite.tela_evento import TelaEvento
from modelo.evento import Evento
#from modelo import pessoa

class ControladorEvento:
    def __init__(self, controlador_principal):
        self.__eventos = []
        self.__controlador_principal = controlador_principal
        self.__tela_evento = TelaEvento(self)

    def pega_evento_por_titulo(self, titulo: str):
        for evento in self.__eventos:
            if(evento.titulo == titulo):
                return evento
        return None
    
    def detalhes_evento(self):
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)
        organizadores = self.nomes_organizadores(evento)
        participantes = self.__controlador_principal.controlador_presenca.nomes_participantes(evento)
        self.__tela_evento.mostra_evento({"titulo": evento.titulo, "data": evento.data, 
                                          "horario_inicio": evento.horario_inicio, 
                                          "local": evento.local, "capacidade_max": evento.capacidade_max,
                                          "organizadores": organizadores, "participantes": participantes})

    def adicionar_evento(self):
            dados_evento = self.__tela_evento.pega_dados_evento()
            pessoa = self.__controlador_principal.controlador_pessoa.busca_pessoa(dados_evento["organizadores"])
            lista_titulos = self.titulos_eventos()
            if dados_evento["titulo"] not in lista_titulos:
                if dados_evento["capacidade_max"].isnumeric() == True:
                    if pessoa is not None:

                        evento = Evento(dados_evento["titulo"], dados_evento["data"], dados_evento["horario_inicio"], 
                                        dados_evento["local"], dados_evento["capacidade_max"], pessoa)
                        self.__eventos.append(evento)
                        self.__tela_evento.mostra_mensagem("Evento adicionado com sucesso!")
                    else:
                        self.__tela_evento.mostra_mensagem("ATENÇÃO: Essa pessoa não existe")
                        self.__tela_evento.mostra_mensagem("O evento não foi adicionado.")
                        self.abre_tela()
                else:
                    self.__tela_evento.mostra_mensagem("ATENÇÃO: A capacidade máxima precisa ser um número inteiro")
                    self.__tela_evento.mostra_mensagem("O evento não foi adicionado.")
                    self.abre_tela()
            else:
                self.__tela_evento.mostra_mensagem("ATENÇÃO: Este título já está sendo utilizado em outro evento")
                self.__tela_evento.mostra_mensagem("O evento não foi adicionado.")
                self.abre_tela()

    def remover_evento(self):
        self.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)

        if(evento is not None):
            self.__eventos.remove(evento)
            self.__tela_evento.mostra_mensagem("O evento foi removido com sucesso")
            self.listar_eventos()
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Este evento não existe.")

    def alterar_evento(self):
        self.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)

        if(evento is not None):
            novos_dados_evento = self.__tela_evento.altera_dados_evento()
            print(novos_dados_evento)
            # if novos_dados_evento["capacidade_max"].isnumeric() == True:

            evento.titulo = novos_dados_evento["titulo"]
            evento.data = novos_dados_evento["data"]
            evento.horario_inicio = novos_dados_evento["horario_inicio"]
            evento.local = novos_dados_evento["local"]
            evento.capacidade_max = int(novos_dados_evento["capacidade_max"])

            # else:
            #     self.__tela_evento.mostra_mensagem("ATENÇÃO: A capacidade máxima precisa ser um número inteiro.")
            #     self.__tela_evento.mostra_mensagem("O evento não foi alterado.")
            #     self.abre_tela()

            self.__tela_evento.mostra_mensagem("Evento alterado com sucesso.")
            self.listar_eventos()
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Este evento não existe.")

    def listar_eventos(self):
        if len(self.__eventos) != 0:
            for evento in self.__eventos:
                organizadores = self.nomes_organizadores(evento)
                participantes = self.__controlador_principal.controlador_presenca.nomes_participantes(evento)
                self.__tela_evento.mostra_evento({"titulo": evento.titulo, "data": evento.data, 
                                                  "horario_inicio": evento.horario_inicio, 
                                                  "local": evento.local, "capacidade_max": evento.capacidade_max,
                                                  "organizadores": organizadores, "participantes": participantes})
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Não existe nenhum evento.")

        #mudar métodos para o Evento

    def titulos_eventos(self):
        lista_titulos = []

        for evento in self.__eventos:
            lista_titulos.append(evento.titulo) 

        return lista_titulos

    def relatório_ranking_evento(self):
        if len(self.__eventos) != 0:
            ranking = 0
            lista_ranking = []
            eventos_ranking = self.__eventos.copy()
            eventos_ranking.sort(reverse=True, key=lambda evento: len(evento.participantes))

            self.__tela_evento.mensagem_ranking()
            tela = []
            for evento in eventos_ranking:
                ranking += 1
                lista_ranking.append(evento.titulo) 
                
                componentes = self.__tela_evento.mostra_ranking(ranking, evento.titulo, len(evento.participantes))
                componentes += tela
                
                
                
            self.__tela_evento.monta_tela()

        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Não existe nenhum evento.")


#------------------------------------- ORGANIZADORES --------------------------------------#

    def adicionar_organizador(self):
        self.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)

        if evento is not None:
            lista = evento.organizadores
            organizador = self.__controlador_principal.controlador_pessoa.busca_pessoa_pelo_nome()

            if organizador is not None:
                if organizador not in lista: 
                    evento.add_organizador(organizador)
                    self.__tela_evento.mostra_mensagem("Organizador adicionado com sucesso.")
                else:
                    self.__tela_evento.mostra_mensagem("ATENÇÃO: Esta pessoa já é organizadora deste evento.")
            else:
                self.abre_tela_2()
        else:
           self.__tela_evento.mostra_mensagem("ATENÇÃO: Esse evento não existe.")
           self.abre_tela_2()
    
    def remover_organizador(self):
        self.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)

        if evento is not None:
            lista = evento.organizadores
            organizador = self.__controlador_principal.controlador_pessoa.busca_pessoa_pelo_nome()

            if organizador is not None:
                if organizador in lista: 
                    evento.del_organizador(organizador)
                    self.__tela_evento.mostra_mensagem("Organizador removido com sucesso.")
                else:
                    self.__tela_evento.mostra_mensagem("ATENÇÃO: Esta pessoa não é organizadora deste evento.")
            else:
                self.abre_tela_2()
        else:
           self.__tela_evento.mostra_mensagem("ATENÇÃO: Esse evento não existe.")
           self.abre_tela_2()

    def nomes_organizadores(self, evento):
        lista_organizadores = evento.organizadores
        lista_nomes = []

        for organizador in lista_organizadores:
            lista_nomes.append(organizador.nome) 

        return lista_nomes

#------------------------------------ TELA --------------------------------------#

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_evento, 2:self.remover_evento, 3:self.alterar_evento, 
        4:self.detalhes_evento, 5:self.listar_eventos, 6: self.relatório_ranking_evento, 
        7: self.abre_tela_2, 0: self.retorna}

        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes()]()

    def abre_tela_2(self):
        lista_opcoes = {1: self.adicionar_organizador, 2:self.remover_organizador, 0: self.retorna_2}

        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes_2()]()

    def retorna(self):
        self.__controlador_principal.abre_tela()
    
    def retorna_2(self):
        self.abre_tela()
