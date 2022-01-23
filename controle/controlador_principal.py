from limite.tela_principal import TelaPrincipal
from controle.controlador_evento import ControladorEvento
from controle.controlador_pessoa import ControladorPessoa
from controle.controlador_presenca import ControladorPresenca

class ControladorPrincipal():
    def __init__(self):
        self.__controlador_evento = ControladorEvento(self)
        self.__controlador_amigos = ControladorPessoa(self)
        self.__controlador_presenca = ControladorPresenca(self)
        self.__tela_principal = TelaPrincipal()