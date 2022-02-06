from modelo.pessoa import Pessoa

class Participante(Pessoa):
  def __init__(self,tipo: str, nome: str, cpf: int, data_nascimento: str, endereco: str, vacina: bool):
    super().__init__(tipo, nome, cpf, data_nascimento, endereco, vacina)
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

    #@teste.setter
    #def teste(self, teste: Teste):
        #if (isinstance(teste, Teste)):
            #self.__teste = teste