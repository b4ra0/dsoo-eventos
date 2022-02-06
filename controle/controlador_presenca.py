from msilib.schema import Class
from controle import controlador_principal
from controle import controlador_evento

from controle.controlador_pessoa import ControladorPessoa
from limite.tela_presenca import TelaPresenca
from controle.controlador_evento import ControladorEvento
from limite.tela_evento import TelaEvento
from modelo.evento import Evento


class ControladorPresenca():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
        self.__tela_presenca = TelaPresenca()
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_evento = ControladorEvento(self)
        self.__tela_evento = TelaEvento(self)

    def adicionar_entrada(self):
        self.__controlador_principal.controlador_evento.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.__controlador_principal.controlador_evento.pega_evento_por_titulo(titulo_evento)
        if evento is not None:
            participante = self.__controlador_principal.controlador_pessoa.busca_pessoa_pelo_nome()
            evento.add_participante(participante)
        else:
           self.__tela_evento.mostra_mensagem("ATENÇÃO: Esse evento não existe.")
        
        
    def verificar_vacina(self):
        pass
    


    def adicionar_saida(self):
        pessoa_saindo = self.__tela_presenca.seleciona_pessoa()
        self.__controlador_pessoa.buscar_pessoa(self, pessoa_saindo)

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_entrada, 2: self.adicionar_saida, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_presenca.tela_opcoes()]()