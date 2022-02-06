from limite.tela_evento import TelaEvento
from modelo.evento import Evento
from modelo import pessoa

class ControladorEvento:
    def __init__(self, controlador_principal):
        self.__eventos = []
        self.__controlador_principal = controlador_principal
        self.__tela_evento = TelaEvento(self)

    def pega_evento_por_titulo(self, titulo: str):
        for evento in self.__eventos:
            if(evento._Evento__titulo == titulo):
                return evento
        return None
    
    def detalhes_evento(self):
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)
        organizadores = self.nomes_organizadores(evento)
        self.__tela_evento.mostra_evento({"titulo": evento._Evento__titulo, "data": evento._Evento__data, 
                                          "horario_inicio": evento._Evento__horario_inicio, 
                                          "local": evento._Evento__local, "capacidade_max": evento._Evento__capacidade_max,
                                          "organizadores": organizadores})

    def adicionar_evento(self):
        dados_evento = self.__tela_evento.pega_dados_evento()

        pessoa = self.__controlador_principal.controlador_pessoa.busca_pessoa(dados_evento["organizadores"])
        #ver situação do nome errado
        
        evento = Evento(dados_evento["titulo"], dados_evento["data"], dados_evento["horario_inicio"], 
                        dados_evento["local"], dados_evento["capacidade_max"], pessoa)
        self.__eventos.append(evento)

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

            evento._Evento__titulo = novos_dados_evento["titulo"]
            evento._Evento__data = novos_dados_evento["data"]
            evento._Evento__horario_inicio = novos_dados_evento["horario_inicio"]
            evento._Evento__local = novos_dados_evento["local"]
            evento._Evento__capacidade_max = novos_dados_evento["capacidade_max"]

            self.__tela_evento.mostra_mensagem("Evento alterado com sucesso.")
            self.listar_eventos()
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Este evento não existe.")

    def listar_eventos(self):
        if len(self.__eventos) != 0:
            for evento in self.__eventos:
                lista_nomes = self.nomes_organizadores(evento)
                print(lista_nomes)
                self.__tela_evento.mostra_evento({"titulo": evento._Evento__titulo, "data": evento._Evento__data, 
                                                  "horario_inicio": evento._Evento__horario_inicio, 
                                                  "local": evento._Evento__local, "capacidade_max": evento._Evento__capacidade_max,
                                                  "organizadores": lista_nomes})
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Não existe nenhum evento.")

    def relatório_ranking_evento(self): #Alterar para pegar por participantes e não organizadores
        if len(self.__eventos) != 0:
            ranking = 0
            lista_ranking = []
            eventos_ranking = self.__eventos.copy()
            eventos_ranking.sort(reverse=True, key=lambda evento: len(evento._Evento__organizadores))

            self.__tela_evento.mensagem_ranking()

            for evento in eventos_ranking:
                ranking += 1
                lista_ranking.append(evento._Evento__titulo) 
                self.__tela_evento.mostra_ranking(ranking, evento._Evento__titulo, len(evento._Evento__organizadores))

        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Não existe nenhum evento.")


#------------------------------------- ORGANIZADORES --------------------------------------#

    def adicionar_organizador(self):
        self.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)

        if evento is not None:
            lista = evento._Evento__organizadores
            organizador = self.__controlador_principal.controlador_pessoa.busca_pessoa_pelo_nome()

            if organizador is not None:
                if organizador not in lista: 
                    evento._Evento__organizadores.append(organizador)
                    self.__tela_evento.mostra_mensagem("Organizador adicionado com sucesso.")
                else:
                    self.__tela_evento.mostra_mensagem("ATENÇÃO: Esta pessoa já é organizadora deste evento.")
            else:
                self.adicionar_organizador()
        else:
           self.__tela_evento.mostra_mensagem("ATENÇÃO: Esse evento não existe.")
           self.adicionar_organizador()
    
    def remover_organizador(self):
        self.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)

        if evento is not None:
            lista = evento._Evento__organizadores
            organizador = self.__controlador_principal.controlador_pessoa.busca_pessoa_pelo_nome()

            if organizador is not None:
                if organizador in lista: 
                    evento._Evento__organizadores.remove(organizador)
                    self.__tela_evento.mostra_mensagem("Organizador removido com sucesso.")
                else:
                    self.__tela_evento.mostra_mensagem("ATENÇÃO: Esta pessoa não é organizadora deste evento.")
            else:
                self.remover_organizador()
        else:
           self.__tela_evento.mostra_mensagem("ATENÇÃO: Esse evento não existe.")
           self.remover_organizador()

    def nomes_organizadores(self, evento):
        lista_organizadores = evento._Evento__organizadores
        lista_nomes = []

        for organizador in lista_organizadores:
            lista_nomes.append(organizador._Pessoa__nome) 

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
