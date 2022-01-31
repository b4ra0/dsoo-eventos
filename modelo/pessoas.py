from eventos import Eventos

class pessoas:
  # fazer aqui tratamento dos dados, caso os parametros sejam diferentes do esperado
  def __init__(self, cpf: int, nome: str, data_nascimento: str, endereco: str, eventos: Eventos):
    self.__cpf = cpf
    self.__nome = nome
    self.__data_nascimento = data_nascimento
    self.__endereco = endereco
    self.__eventos = Eventos

    @property
    def cpf(self):
        return self.__cpf

    @property
    def nome(self):
        return self.__nome

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def eventos(self):
        return self.__eventos

    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = data_nascimento

    @eventos.setter
    def eventos(self, eventos: str):
        self.__eventos = eventos