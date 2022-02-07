#from modelo.evento import Evento

class Pessoa:
  def __init__(self, tipo: str, nome: str, cpf: int, data_nascimento: str, endereco: str, vacina: int):
    self.__tipo = tipo
    self.__nome = nome
    self.__cpf = cpf
    self.__data_nascimento = data_nascimento
    self.__endereco = endereco
    self.__evento = []
    self.__vacina = vacina

    @property
    def tipo(self):
        return self.__tipo

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @tipo.setter
    def tipo(self, tipo: str):
        self.__tipo = tipo

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome
    
    @cpf.setter
    def cpf(self, cpf: int):
        self.__cpf = cpf

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = data_nascimento