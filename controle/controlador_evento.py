

from limite.tela_evento import TelaEvento
from modelo.evento import Evento

class ControladorEvento:
    def __init__(self, controlador_principal):
        self.__eventos = []
        self.__controlador_principal = controlador_principal
        self.__tela_evento = TelaEvento()

    def pega_evento_por_titulo(self):
        for evento in self.__eventos:
            if(evento.titulo == titulo):
                return evento
        return None
    
    def detalhes_evento(self):
        self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo()
        self.__tela_evento.mostra_evento()

    def adicionar_evento(self):
        dados_evento = self.__tela_evento.pega_dados_evento()
        evento = Evento(dados_evento["titulo"], dados_evento["data"], dados_evento["horario_inicio"], 
                        dados_evento["local"], dados_evento["capacidade_max"], dados_evento["organizador"])
        self.__eventos.append(evento)

    def remover_evento(self):
        self.lista_evento()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo()

        if(evento is not None):
            self.__eventos.remove(evento)
            self.lista_evento()
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Este evento não existe.")

    def alterar_evento(self):
        self.lista_evento()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.pega_evento_por_titulo(titulo_evento)

        if(evento is not None):
            novos_dados_evento = self.__tela_evento.pega_dados_evento()
            evento.titulo = novos_dados_evento["titulo"]
            evento.data = novos_dados_evento["data"]
            evento.horario_inicio = novos_dados_evento["horario_inicio"]
            evento.local = novos_dados_evento["local"]
            evento.capacidade_max = novos_dados_evento["capacidade_max"]
            evento.organizador = novos_dados_evento["organizador"]
            self.lista_evento()
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Este evento não existe.")

    def lista_evento(self):
        if len(self.__eventos) != 0:
            for evento in self.__eventos:
                self.__tela_evento.mostra_evento({"titulo": evento.titulo, "data": evento.data, 
                                                  "horario_inicio": evento.horario_inicio, 
                                                  "local": evento.local, "capacidade_max": evento.capacidade_max,
                                                  "organizador": evento.organizador})
        else:
            self.__tela_evento.mostra_mensagem("ATENÇÃO: Não existe nenhum evento.")

    def ranking_evento(self):
        ranking = 1
        for i in range(len(self.__eventos)):
            ranking += 1

    def abre_tela(self):
        self.lista_opcoes = {1: self.adicionar_evento, 2:self.remover_evento, 3:self.alterar_evento, 4: 
                             self.detalhes_evento, 5:self.lista_evento, 6: self.ranking_evento, 0: self.retorna}
        continua = True
        while continua:
            lista_opcoes = [self.__tela_evento.tela_opcoes()]()

    def retorna(self):
        self.__controlador_principal.abre_tela()