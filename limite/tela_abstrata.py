from abc import ABC, abstractmethod
from multiprocessing.sharedctypes import Value

class TelaAbstrata(ABC):

    @abstractmethod
    def le_num_inteiro(self, mensagem: str = "", inteiros_validos = None):
        while True:
            valor_lido = input(mensagem)
            try:
                inteiro = int(valor_lido)
                if inteiros_validos and inteiro not in inteiros_validos:
                    raise ValueError
                return inteiro
            except ValueError:
                print("Valor incorreto: Digite um valor numérico inteiro valido")
                if inteiros_validos:
                    print("Valores validos: ", inteiros_validos)
                

