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
            if int(evento.capacidade_max) > len(evento.participantes):
                participante = self.__controlador_principal.controlador_pessoa.busca_pessoa_pelo_nome()
                if participante not in evento.participantes:
                    if int(participante.vacina) == True:
                        evento.add_participante(participante)
                        self.__tela_evento.mostra_mensagem("Participante adicionado com sucesso!!")
                    else:
                        self.__tela_evento.mostra_mensagem("ATENÇÃO: Você precisa estar vacinado ou com o teste negativo")
                        dados_teste = self.__tela_presenca.tela_teste()
                        if dados_teste["resultado"] != True:
                                if int(dados_teste["horas"]) <= 72:
                                    evento.add_participante(participante)
                                    self.__tela_evento.mostra_mensagem("Participante adicionado com sucesso!!")
                                else:
                                    self.__tela_evento.mostra_mensagem("ATENÇÃO: Seu teste de COVID-19 não é mais válido, deve ser feito 72h antes do evento!")
                        else:
                            self.__tela_evento.mostra_mensagem("ATENÇÃO: Seu teste de COVID-19 deu positivo, você não pode entrar!")
                else:
                    self.__tela_evento.mostra_mensagem("ATENÇÃO: Essa pessoa já é um participante deste evento!")
            else:
                self.__tela_evento.mostra_mensagem("ATENÇÃO: Limite de participantes atingido")
        else:
           self.__tela_evento.mostra_mensagem("ATENÇÃO: Esse evento não existe!")
    


    def adicionar_saida(self):
        self.__controlador_principal.controlador_evento.listar_eventos()
        titulo_evento = self.__tela_evento.seleciona_evento()
        evento = self.__controlador_principal.controlador_evento.pega_evento_por_titulo(titulo_evento)
        if evento is not None:
            participante = self.__controlador_principal.controlador_pessoa.busca_pessoa_pelo_nome()
            if participante in evento.participantes:
                evento.del_participante(participante)
                self.__tela_evento.mostra_mensagem("Participante removido com sucesso!!")
            else:
                self.__tela_evento.mostra_mensagem("ATENÇÃO: Essa pessoa não é um participante deste evento")
        else:
           self.__tela_evento.mostra_mensagem("ATENÇÃO: Esse evento não existe.")


    def nomes_participantes(self, evento):
        lista_participantes = evento.participantes
        lista_nomes = []
        if len (evento.participantes) != 0:
            for participante in lista_participantes:
                lista_nomes.append(participante.nome)

        return lista_nomes
    

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_entrada, 2: self.adicionar_saida, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_presenca.tela_opcoes()]()