from . import Teste
from pessoas import Pessoas

class participantes(Pessoas):
  def __init__(self, vacina: bool, teste: Teste, cpf: int, nome: str, data_nascimento: str, endereco: str, eventos: Eventos):
    super().__init__(cpf, nome, data_nascimento, endereco, eventos)
    self.__vacina = vacina
    self.__teste = Teste
    self.__pessoa = Pessoas

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