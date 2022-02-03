from limite.tela_pessoa import TelaPessoa
from modelo.pessoa import Pessoa

class ControladorPessoa():
    def __init__(self, controlador_principal):
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_principal = controlador_principal

    def busca_pessoa(self, nome: str):
        for pessoinha in self.__pessoas:
            if(pessoinha._Pessoa__nome == nome):
                return pessoinha
        return None

    def incluir_pessoa(self):
        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        pessoa = Pessoa(dados_pessoa["nome"], dados_pessoa["cpf"], dados_pessoa["data_nascimento"], dados_pessoa["endereco"])
        self.__pessoas.append(pessoa)

    def alterar_pessoa(self):
        self.lista_pessoa()
        nome_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.busca_pessoa(nome_pessoa)

        if(pessoa is not None):
            novos_dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
            pessoa._Pessoa__nome = novos_dados_pessoa["nome"]
            pessoa._Pessoa__cpf = novos_dados_pessoa["cpf"]
            pessoa._Pessoa__data_nascimento = novos_dados_pessoa["data_nascimento"]
            pessoa._Pessoa__endereco = novos_dados_pessoa["endereco"]
            self.lista_pessoa()
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Pessoa não existente")
    
    def excluir_pessoa(self):
        self.lista_pessoa()
        nome_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.busca_pessoa(nome_pessoa)

        if(pessoa is not None):
            self.__pessoas.remove(pessoa)
            self.lista_pessoa()
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Pessoa não existente")

    def lista_pessoa(self):
        for pessoinha in self.__pessoas:
            self.__tela_pessoa.mostra_pessoa({"cpf": pessoinha._Pessoa__cpf, "nome": pessoinha._Pessoa__nome, 
                                              "data_nascimento": pessoinha._Pessoa__data_nascimento, "endereco": pessoinha._Pessoa__endereco})

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.incluir_pessoa, 2: self.alterar_pessoa, 3: self.lista_pessoa, 4: self.excluir_pessoa, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()
