

from limite.tela_evento import TelaEvento
from modelo.evento import Evento

class ControladorEventos:
    def __init__(self, controlador_principal):
        self.__eventos = []
        self.__controlador_principal = controlador_principal
        self.__tela_eventos = TelaEvento()

    def adicionar_evento(self):
        dados_evento = self.__tela_eventos.pega_dados_evento()
        evento = Evento(dados_evento["titulo"], dados_evento["data"], dados_evento["horario_inicio"], 
                        dados_evento["local"], dados_evento["capacidade_max"], dados_evento["organizador"])
        self.__eventos.append(evento)

    def remover_evento(self):
        titulo_evento = self.__tela_eventos.seleciona_evento()
        amigo = None

    def detalhes_evento(self):
        pass

    def alterar_evento(self):
        pass

    def lista_evento(self):
        pass

    def ranking_evento(self):
        pass

    def abre_tela(self):
        pass

    def retorna(self):
        pass 