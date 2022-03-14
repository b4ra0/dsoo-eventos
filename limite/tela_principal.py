from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPrincipal(TelaAbstrata):

    def tela_opcoes(self):
        layout = [
            [sg.Text('Gerenciador Biguizel!')],
            [sg.Submit(button_text=('Eventos'), key='1')],
            [sg.Submit(button_text=('Pessoas'), key='2')],
            [sg.Submit(button_text=('Presença'), key='3')],
            [sg.Submit(button_text=('Finalizar o sistema'), key='0')]
        ]

        window = sg.Window('Pagina Principal', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button)
    
    def le_num_inteiro(self, mensagem: str = "", inteiros_validos=None):
        return super().le_num_inteiro(mensagem, inteiros_validos)


