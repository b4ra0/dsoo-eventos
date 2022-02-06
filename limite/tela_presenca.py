class TelaPresenca():
  def tela_opcoes(self):
    print("-------- PRESENÇA ----------")
    print("Escolha a opcao")
    print("1 - Adicionar entrada")
    print("2 - Adicionar saída")
    print("0 - Retornar")

    opcao = int(input("Escolha a opção: "))
    return opcao
    
  def seleciona_pessoa(self):
    nome = input("Nome da pessoa que deseja selecionar: ")
    return nome
