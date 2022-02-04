from limite.tela_evento import TelaEvento
from modelo.evento import Evento

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
        self.__tela_evento.mostra_evento({"titulo": evento._Evento__titulo, "data": evento._Evento__data, 
                                          "horario_inicio": evento._Evento__horario_inicio, 
                                          "local": evento._Evento__local, "capacidade_max": evento._Evento__capacidade_max,
                                          "organizador": evento._Evento__organizador})

    def adicionar_evento(self):
        dados_evento = self.__tela_evento.pega_dados_evento()
        evento = Evento(dados_evento["titulo"], dados_evento["data"], dados_evento["horario_inicio"], 
                        dados_evento["local"], dados_evento["capacidade_max"], dados_evento["organizador"])
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
            novos_dados_evento = self.__tela_evento.pega_dados_evento()
            evento._Evento__titulo = novos_dados_evento["titulo"]
            evento._Evento__data = novos_dados_evento["data"]
            evento._Evento__horario_inicio = novos_dados_evento["horario_inicio"]
            evento._Evento__local = novos_dados_evento["local"]
            evento._Evento__capacidade_max = novos_dados_evento["capacidade_max"]
            evento._Evento__organizador = novos_dados_evento["organizador"]
            self.listar_eventos()
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Este evento não existe.")

    def listar_eventos(self):
        if len(self.__eventos) != 0:
            for evento in self.__eventos:
                self.__tela_evento.mostra_evento({"titulo": evento._Evento__titulo, "data": evento._Evento__data, 
                                                  "horario_inicio": evento._Evento__horario_inicio, 
                                                  "local": evento._Evento__local, "capacidade_max": evento._Evento__capacidade_max,
                                                  "organizador": evento._Evento__organizador})
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Não existe nenhum evento.")

    def relatório_ranking_evento(self):
        eventos_ranking = self.__eventos.copy()
        for evento in self.__eventos:
            for evento_ranking in eventos_ranking:
                if len(evento.participantes) > len(evento_ranking.participantes):
                    anterior = eventos_ranking[eventos_ranking.index(evento_ranking)]
                    eventos_ranking[0] = evento
                    #ir reordenando a lista de eventos_ranking


        return eventos_ranking

    def adicionar_organizador(self): #Não funcional
        self.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)
        if evento is not None:
            organizador = self.__controlador_principal.controlador_pessoa.busca_pessoa()
            evento.add_organizador(organizador)
        else:
           self.__tela_evento.mostra_mensagem("ATENÇÃO: Esse evento não existe.")
    
    def remover_organizador(self):
        pass

    def adicionar_participante(self):
        pass

    def remover_participante(self):
        pass

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_evento, 2:self.remover_evento, 3:self.alterar_evento, 
        4:self.detalhes_evento, 5:self.listar_eventos, 6: self.relatório_ranking_evento, 
        7: self.abre_tela_2, 0: self.retorna}

        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes()]()

    def abre_tela_2(self):
        lista_opcoes = {1: self.adicionar_organizador, 2:self.remover_organizador,
         3:self.adicionar_participante, 4:self.adicionar_organizador, 0: self.retorna_2}

        continua = True
        while continua:
            lista_opcoes[self.__tela_evento.tela_opcoes_2()]()

    def retorna(self):
        self.__controlador_principal.abre_tela()
    
    def retorna_2(self):
        self.abre_tela()