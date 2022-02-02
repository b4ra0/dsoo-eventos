from limite.tela_pessoas import TelaPessoas
from modelo.pessoas import Pessoas

class ControladorPessoas():
    def __init__(self, controlador_principal):
        self.__pessoas = []
        self.__tela_pessoas = TelaPessoas()
        self.__controlador_principal = controlador_principal

    def busca_pessoa(self, nome: str):
        for pessoas in self.__pessoas:
            if(pessoas.nome == nome):
                return pessoas
        return None

    def incluir_pessoa(self):
        dados_pessoa = self.__tela_pessoas.pega_dados_pessoa()
        pessoa = Pessoas(dados_pessoa["nome"], dados_pessoa["cpf"], dados_pessoa["data_nascimento"], dados_pessoa["endereco"])
        self.__pessoas.append(pessoa)

    def alterar_pessoa(self):
        self.lista_pessoas()
        nome_pessoa = self.__tela_pessoas.seleciona_pessoa()
        pessoa = self.busca_pessoa(nome_pessoa)

        if(pessoa is not None):
            novos_dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
            pessoa.nome = novos_dados_pessoa["nome"]
            pessoa.telefone = novos_dados_pessoa["telefone"]
            pessoa.cpf = novos_dados_pessoa["cpf"]
            self.lista_pessoas()
        else:
            self.__tela_pessoa.mostra_mensagem("ATENCAO: pessoa não existente")


    def lista_pessoas(self):
        for pessoas in self.__pessoas:
            self.__tela_pessoas.mostra_pessoa({"nome": pessoas.nome, "cpf": pessoas.cpf, "data_nascimento": pessoas.data_nascimento, "endereco": pessoas.endereco})

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_pessoas, 2: self.alterar_pessoas, 3: self.lista_pessoas, 4: self.excluir_pessoas, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
