from limite.tela_principal import TelaPrincipal
from controle.controlador_evento import ControladorEvento
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_presenca import ControladorPresenca

class ControladorPrincipal():
    def __init__(self):
        self.__controlador_evento = ControladorEvento(self)
        self.__controlador_pessoa = ControladorPessoa(self)
        self.__controlador_presenca = ControladorPresenca(self)
        self.__tela_principal = TelaPrincipal()

    @property
    def controlador_evento(self):
        return self.__controlador_evento

    @property
    def controlador_pessoa(self):
        return self.__controlador_pessoa

    @property
    def controlador_presenca(self):
        return self.__controlador_presenca

    def inicializa_sistema(self):
        self.abre_tela()

    def abre_tela_evento(self):
        self.__controlador_evento.abre_tela()

    def abre_tela_pessoa(self):
        self.__controlador_pessoa.abre_tela()

    def abre_tela_presenca(self):
        self.__controlador_presenca.abre_tela()

    def encerra_sistema(self):
        exit(0)

    def abre_tela(self):
        lista_opcoes = {1: self.abre_tela_evento, 2: self.abre_tela_pessoa,
                        3:self.abre_tela_presenca, 0: self.encerra_sistema}

        while True:
            opcao_escolhida = self.__tela_principal.tela_opcoes()
            funcao_escolhida = lista_opcoes[opcao_escolhida]
            funcao_escolhida()