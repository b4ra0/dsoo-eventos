from msilib.schema import Class

from controle.controlador_pessoa import ControladorPessoa


class ControladorPresenca():
    def __init__(self, controlador_principal):
        self.__controlador_principal = controlador_principal
    #def adicionar_entrada(self):


    #def adicionar_saida(self):


    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_entrada, 2: self.adicionar_saida, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()