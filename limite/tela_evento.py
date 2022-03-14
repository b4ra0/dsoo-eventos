from limite.tela_abstrata import TelaAbstrata
from modelo import evento
import PySimpleGUI as sg

class TelaEvento(TelaAbstrata):

    def __init__(self, controlador_evento):
        self.__controlador_evento = controlador_evento

    def tela_opcoes(self):

        layout = [
            [sg.Text('EVENTOS')],
            [sg.Submit(button_text=('Adicionar evento'), key='1')],
            [sg.Submit(button_text=('Remover evento'), key='2')],
            [sg.Submit(button_text=('Alterar evento'), key='3')],
            [sg.Submit(button_text=('Detalhe evento'), key='4')],
            [sg.Submit(button_text=('Listar eventos'), key='5')],
            [sg.Submit(button_text=('Ranking eventos'), key='6')],
            [sg.Submit(button_text=('Organizadores dos eventos (+)'), key='7')],
            [sg.Submit(button_text=('Retornar'), key='0')],
        ]

        window = sg.Window('Tela Eventos', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button)

    def tela_opcoes_2(self):
        layout = [
            [sg.Text('ORGANIZADORES DOS EVENTOS')],
            [sg.Submit(button_text=('Adicionar organizador em evento'), key='1')],
            [sg.Submit(button_text=('Remover organizador de evento'), key='2')],
            [sg.Submit(button_text=('Retornar'), key='0')],
        ]

        window = sg.Window('Organizadores do evento', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()
        return int(button)


    def le_num_inteiro(self, mensagem: str = "", inteiros_validos=None):
        return super().le_num_inteiro(mensagem, inteiros_validos)

#---------------------------------------------------------------------------------

    def pega_dados_evento(self):
        layout = [
            [sg.Text('PEGAR DADOS DO EVENTO')],
            [sg.Text('Título do evento: '), sg.InputText(key='titulo')],
            [sg.Text('Data do evento: '), sg.InputText(key='data')],
            [sg.Text('Horário de início do evento: '), sg.InputText(key='horario_inicio')],
            [sg.Text('Local do evento: '), sg.InputText(key='local')],
            [sg.Text('Capacidade máxima do evento: '), sg.InputText(key='capacidade_max')],
            [sg.Text('Organizadores do evento: '), sg.InputText(key='organizadores')],
            [sg.Submit(button_text=('Aceitar'))]
        ]
        window = sg.Window('Pegar dados do evento', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()
        return(values)

    def altera_dados_evento(self):
        layout = [
            [sg.Text('ALTERAR DADOS DO EVENTO')],
            [sg.Text('Título do evento: '), sg.InputText(key='titulo')],
            [sg.Text('Data do evento: '), sg.InputText(key='data')],
            [sg.Text('Horário de início do evento: '), sg.InputText(key='horario_inicio')],
            [sg.Text('Local do evento: '), sg.InputText(key='local')],
            [sg.Text('Capacidade máxima do evento: '), sg.InputText(key='capacidade_max')],
            [sg.Submit(button_text=('Aceitar'))]
        ]
        window = sg.Window('Alterar dados do evento', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()
        titulo = values["titulo"]
        return(values)

    def mostra_evento(self, dados_evento):
        layout = [
            [sg.Text("TÍTULO DO EVENTO: "), sg.Text(dados_evento["titulo"])],
            [sg.Text("DATA DO EVENTO: "), sg.Text(dados_evento["data"])],
            [sg.Text("HORARIO DE INÍCIO: "), sg.Text(dados_evento["horario_inicio"])],
            [sg.Text("LOCAL DO EVENTO: "), sg.Text(dados_evento["local"])],
            [sg.Text("CAPACIDADE MÁXIMA DO EVENTO: "), sg.Text(dados_evento["capacidade_max"])],
            [sg.Text("ORGANIZADORES DO EVENTO: "), sg.Text(dados_evento["organizadores"])],
            [sg.Text("PARTICIPANTES DO EVENTO: "), sg.Text(dados_evento["participantes"])],
        ]
        window = sg.Window('Mostra evento', element_justification='center').Layout(layout)
        values = window.Read()

    def seleciona_evento(self):
        layout = [
            [sg.Text('Título'), sg.InputText(key='titulo')],
            [sg.Button('Buscar')],
        ]
        window = sg.Window('Seleciona evento', element_justification='center').Layout(layout)
        button, values = window.Read()
        titulo = values["titulo"]
        window.close()
        return titulo

    def mensagem_ranking(self):
        print("\n")
        print("----- RANKING DE EVENTOS POR PARTICIPANTES -----")
        print("\n")
        

    def mostra_ranking(self, ranking, titulo, n_participantes):
        layout = [
            [sg.Text(ranking), sg.Text('-'), sg.Text(titulo)],
            [sg.Text('Nº de participantes:', sg.Text(n_participantes))],
            [sg.Text(' ')],
        ]
        return layout

    def monta_tela(self):
        window = sg.Window('Mostra ranking', element_justification='center').Layout(self.__controlador_evento.relatório_ranking_evento.tela)
        a,b = window.Read()

    def mostra_mensagem(self, msg):
        layout = [
            [sg.Text(msg)],
            [sg.Button('Ok')],
        ]
        window = sg.Window('Mensagem', element_justification='center').Layout(layout)
        button, values = window.Read()
        window.close()