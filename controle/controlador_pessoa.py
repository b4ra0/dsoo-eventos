from limite.tela_pessoa import TelaPessoa
from modelo.participante import Participante
from modelo.pessoa import Pessoa

class ControladorPessoa():
    def __init__(self, controlador_principal):
        self.__pessoas = []
        self.__tela_pessoa = TelaPessoa()
        self.__controlador_principal = controlador_principal

    def busca_pessoa(self, nome: str):
        for pessoa in self.__pessoas:
            print("Pessoa", pessoa)
            if(pessoa._Pessoa__nome == nome):
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
        print(dados_pessoa)
        #verificar se já existe outra pessoa com o nome
        pessoa = Participante(dados_pessoa["tipo"], dados_pessoa["nome"], dados_pessoa["cpf"], dados_pessoa["data_nascimento"], dados_pessoa["endereco"], dados_pessoa["vacina"])
        self.__pessoas.append(pessoa) #vacina: bool, cpf: int, nome: str, data_nascimento: str, endereco: str

    def alterar_pessoa(self):
        self.listar_pessoa()
        nome_pessoa = self.__tela_pessoa.seleciona_pessoa()
        pessoa = self.busca_pessoa(nome_pessoa)

        if(pessoa is not None):
            novos_dados_pessoa = self.__tela_pessoa.pega_dados_pessoa()
            pessoa._Pessoa__tipo = novos_dados_pessoa["tipo"]
            pessoa._Pessoa__nome = novos_dados_pessoa["nome"]
            pessoa._Pessoa__cpf = novos_dados_pessoa["cpf"]
            pessoa._Pessoa__data_nascimento = novos_dados_pessoa["data_nascimento"]
            pessoa._Pessoa__endereco = novos_dados_pessoa["endereco"]
            pessoa._Pessoa__vacina = novos_dados_pessoa["vacina"]
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
                self.__tela_pessoa.mostra_pessoa({"tipo": pessoa._Pessoa__tipo, "cpf": pessoa._Pessoa__cpf, "nome": pessoa._Pessoa__nome, 
                                                "data_nascimento": pessoa._Pessoa__data_nascimento, 
                                                "endereco": pessoa._Pessoa__endereco, "vacina": pessoa._Pessoa__vacina})
        else:
            self.__tela_pessoa.mostra_mensagem("ATENÇÃO: Não existe nenhuma pessoa.")

            #Lista participantes e organizadores

    def retornar(self):
        self.__controlador_principal.abre_tela()

    def abre_tela(self):
        lista_opcoes = {1: self.adicionar_pessoa, 2: self.alterar_pessoa, 3: self.listar_pessoa, 4: self.remover_pessoa, 0: self.retornar}
        continua = True
        while continua:
            lista_opcoes[self.__tela_pessoa.tela_opcoes()]()