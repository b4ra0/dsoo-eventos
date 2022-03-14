from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPessoa(TelaAbstrata):

    def tela_opcoes(self):

        layout = [
            [sg.Text('PESSOAS')],
            [sg.Submit(button_text=('Adicionar Pessoa'), key='1')],
            [sg.Submit(button_text=('Alterar pessoa'), key='2')],
            [sg.Submit(button_text=('Listar Pessoa'), key='3')],
            [sg.Submit(button_text=('Excluir Pessoa'), key='4')],
            [sg.Submit(button_text=('Retornar'), key='0')],
        ]

        window = sg.Window('Tela Pessoas', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button)

    def le_num_inteiro(self, mensagem: str = "", inteiros_validos=None):
        return super().le_num_inteiro(mensagem, inteiros_validos)

    def pega_dados_pessoa(self):
        layout = [
            [sg.Text('ADICIONAR PESSOAS')],
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Text('CPF'), sg.InputText(key='cpf')],
            [sg.Text('Data de Nascimento'), sg.InputText(key='data_nascimento')],
            [sg.Text('Endereço'), sg.InputText(key='endereco')],
            [sg.Text('Vacina'), sg.Radio('Dose completa', "RADIO1", key="vacina_completa"), sg.Radio('Não completa', "RADIO1", key="vacina_incompleta")],
            [sg.Submit(button_text=('Aceitar'))]
        ]
        window = sg.Window('Adicionar pessoas', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()
        print(values)
        return(values)

    def mostra_pessoa(self, dados_pessoa):
        layout = [
            [sg.Text('Nome'), sg.Text(dados_pessoa["nome"])],
            [sg.Text('CPF'), sg.Text(dados_pessoa["cpf"])],
            [sg.Text('Data de Nascimento'), sg.Text(dados_pessoa["data_nascimento"])],
            [sg.Text('Endereço'), sg.Text(dados_pessoa["endereco"])],
            [sg.Text('Vacina'), sg.Text(dados_pessoa["vacina"])],
        ]
        window = sg.Window('Mostra pessoa', element_justification='center').Layout(layout)
        button, values = window.Read()
        
    def seleciona_pessoa(self):
        layout = [
            [sg.Text('Nome'), sg.InputText(key='nome')],
            [sg.Button('Buscar')],
        ]
        window = sg.Window('Seleciona pessoa', element_justification='center').Layout(layout)
        button, values = window.Read()
        nome = values["nome"]
        window.close()
        print (nome),
        return nome

    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg)],
            [sg.Button('Ok')],
        ]
        window = sg.Window('Mensagem', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()
