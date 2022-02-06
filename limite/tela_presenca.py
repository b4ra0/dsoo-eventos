from limite.tela_abstrata import TelaAbstrata

class TelaPresenca(TelaAbstrata):

  def tela_opcoes(self):
    print("-------- PRESENÇA ----------")
    print("Escolha a opcao")
    print("1 - Adicionar entrada")
    print("2 - Adicionar saída")
    print("0 - Retornar")

    opcao = self.le_num_inteiro("Escolha uma opção: ", [1, 2, 0])
    return opcao

  def le_num_inteiro(self, mensagem: str = "", inteiros_validos=None):
      return super().le_num_inteiro(mensagem, inteiros_validos)
    
  def seleciona_pessoa(self):
    nome = input("Nome da pessoa que deseja selecionar: ")
    return nome
