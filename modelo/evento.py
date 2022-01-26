from modelo.organizador import Organizador
from modelo.participante import Participante

class Evento:

    def __init__(self, titulo: str, data: str, horario_inicio: str, local: str, capacidade_max: int, organizadores: Organizador):
        self.__titulo = titulo
        self.__data = data
        self.__horario_inicio = horario_inicio
        self.__local = local
        self.__capacidade_max = capacidade_max
        self.__organizadores = Organizador #Aqui vai Pessoa?
        self.__participantes = None 

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
  
        @organizadores.setter
        def organizadores(self,organizadores: Organizador):
            if isinstance(organizadores, Organizador):
                self.__organizadores = organizadores

        @property
        def participantes(self):
            return self.__participantes
  
        @participantes.setter
        def participantes(self,participantes: Participante): #Pessoa também?
            if isinstance(participantes, Participante):
                self.__participantes = participantes
'''

def main():
    teste_lindo = Evento("Pixel Init","05/01/2022","18:00", "Online", 12)
    print(teste_lindo._Evento__titulo)
main()

'''