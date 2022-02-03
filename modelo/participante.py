from . import Teste
from pessoa import Pessoa

class Participante(Pessoa):
  def __init__(self, vacina: bool, cpf: int, nome: str, data_nascimento: str, endereco: str):
    super().__init__(cpf, nome, data_nascimento, endereco)
    self.__vacina = vacina
    self.__teste = None
    self.__pessoa = Pessoa

    @property
    def vacina(self):
        return self.__vacina

    @property
    def teste(self):
        return self.__teste

    @vacina.setter
    def vacina(self, vacina: bool):
        self.__vacina = vacina

    @teste.setter
    def teste(self, teste: Teste):
        if (isinstance(teste, Teste)):
            self.__teste = teste