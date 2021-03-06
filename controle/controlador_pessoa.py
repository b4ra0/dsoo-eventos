from limite.tela_pessoa import TelaPessoa
from modelo.pessoa import Pessoa

class ControladorPessoa():
    def __init__(self, controlador_principal):
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_principal = controlador_principal


    def busca_pessoa(self, nome: str):
        for pessoa in self.__pessoas:
            if(pessoa.nome == nome):
                return pessoa
        return None

    def busca_pessoa_pelo_nome(self):
        nome = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.busca_pessoa(nome)
        if pessoa is not None:
            return pessoa
        else: 
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Pessoa não existente")

    def adicionar_pessoa(self):

        dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
        lista_nomes = self.nomes_pessoas()
        if dados_pessoa["nome"] not in lista_nomes:
            pessoa = Pessoa(dados_pessoa["nome"], dados_pessoa["cpf"], 
                                dados_pessoa["data_nascimento"], dados_pessoa["endereco"], dados_pessoa["vacina_completa"])
            self.__pessoas.append(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa adicionada com sucesso")
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: O nome desta pessoa já está sendo utilizado!")
            self.abre_tela()

    def alterar_pessoa(self):
        self.listar_pessoa()
        nome_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.busca_pessoa(nome_pessoa)

        if(pessoa is not None):
            novos_dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
            pessoa.nome = novos_dados_pessoa["nome"]
            pessoa.cpf = novos_dados_pessoa["cpf"]
            pessoa.data_nascimento = novos_dados_pessoa["data_nascimento"]
            pessoa.endereco = novos_dados_pessoa["endereco"]
            pessoa.vacina = novos_dados_pessoa["vacina_completa"]
            self.listar_pessoa()
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Pessoa não existente")
    
    def remover_pessoa(self):
        self.listar_pessoa()
        nome_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.busca_pessoa(nome_pessoa) #if

        if(pessoa is not None):
            self.__pessoas.remove(pessoa)
            self.__tela_pessoa.mostra_mensagem("Pessoa removida com sucesso")
            self.listar_pessoa()
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Pessoa não existente")


    def listar_pessoa(self):
        if len(self.__pessoas) != 0:
            for pessoa in self.__pessoas:
                self.__tela_pessoa.mostra_pessoa({"cpf": pessoa.cpf, "nome": pessoa.nome, 
                                                  "data_nascimento": pessoa.data_nascimento, 
                                                  "endereco": pessoa.endereco, "vacina": pessoa.vacina})
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Não existe nenhuma pessoa.")

    def nomes_pessoas(self):
        lista_nomes = []
        for pessoa in self.__pessoas:
            lista_nomes.append(pessoa.nome) 

        return lista_nomes

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_pessoa, 2: self.alterar_pessoa, 
                        3: self.listar_pessoa, 4: self.remover_pessoa, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()