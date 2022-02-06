from limite.tela_abstrata import TelaAbstrata

class TelaPrincipal(TelaAbstrata):

    def tela_opcoes(self):
        print("-------- GERENCIADOR BIGUIZEL --------")
        print("Escolha sua opcao")
        print("1 - Eventos")
        print("2 - Pessoas")
        print("3 - Presença")
        print("0 - Finalizar sistema")
        opcao = self.le_num_inteiro("Escolha uma opção: ", [1, 2, 3, 0])
        return opcao
    
    def le_num_inteiro(self, mensagem: str = "", inteiros_validos=None):
        return super().le_num_inteiro(mensagem, inteiros_validos)