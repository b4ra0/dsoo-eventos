from modelo.organizador import Organizador
from modelo.participante import Participante
from modelo.pessoa import Pessoa

class Evento:

    def __init__(self, titulo: str, data: str, horario_inicio: str, local: str, capacidade_max: int, organizador: Organizador):
        self.__titulo = titulo
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__local = local
        #Ao adicionar um evento, ainda é possível atribuir um str à capacidade max
        self.__capacidade_max = capacidade_max
        self.__organizador = organizador
        self.__organizadores = []
        self.__organizadores.append(organizador)
        self.__participantes = []

        @property
        def titulo(self):
            return self.__titulo
  
        @titulo.setter
        def titulo(self,titulo: str):
            if isinstance(titulo, str):
                self.__titulo = titulo

        @property
        def data(self):
            return self.__data
  
        @data.setter
        def data(self,data: str):
            if isinstance(data, str):
                self.__data = data

        @property
        def horario_inicio(self):
            return self.__horario_inicio
  
        @horario_inicio.setter
        def horario_inicio(self,horario_inicio: str):
            if isinstance(horario_inicio, str):
                self.__horario_inicio = horario_inicio

        @property
        def local(self):
            return self.__local
  
        @local.setter
        def local(self,local: str):
            if isinstance(local, str):
                self.__local = local

        @property
        def capacidade_max(self):
            return self.__capacidade_max
  
        @capacidade_max.setter
        def capacidade_max(self,capacidade_max: int):
            if isinstance(capacidade_max, int):
                self.__capacidade_max = capacidade_max

        @property
        def organizadores(self):
            return self.__organizadores
        
        def add_organizador(self,organizador: Pessoa):
            if isinstance(organizador, Pessoa):
                self.__organizadores.append(organizador)

        def del_organizador(self,organizador: Organizador):
            if isinstance(organizador, Organizador):
                self.__organizadores.remove(organizador)    

        @property
        def participantes(self):
            return self.__participantes

        def add_participante(self, participante: Participante):
            if isinstance(participante, Participante):
                self.__participantes.append(participante)

        def del_participante(self, participante: Participante):
            if isinstance(participante, Participante):
                self.__participantes.remove(participante)