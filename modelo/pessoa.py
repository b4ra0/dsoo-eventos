
class Pessoa:
    def __init__(self, nome: str, cpf: str, data_nascimento: str, endereco: str, vacina: int):
        self.__nome = nome
        self.__cpf = cpf
        self.__data_nascimento = data_nascimento
        self.__endereco = endereco
        self.__vacina = vacina

    @property
    def nome(self):
        return self.__nome

    @property
    def cpf(self):
        return self.__cpf

    @property
    def data_nascimento(self):
        return self.__data_nascimento

    @property
    def endereco(self):
        return self.__endereco

    @property
    def vacina(self):
        return self.__vacina

    @nome.setter
    def nome(self, nome: str):
        self.__nome = nome

    @cpf.setter
    def cpf(self, cpf: str):
        self.__cpf = cpf

    @vacina.setter
    def vacina(self, vacina: int):
        self.__vacina = vacina

    @data_nascimento.setter
    def data_nascimento(self, data_nascimento: str):
        self.__data_nascimento = data_nascimento

    @endereco.setter
    def endereco(self, endereco: str):
        self.__endereco = endereco