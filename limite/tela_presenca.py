from limite.tela_abstrata import TelaAbstrata
import PySimpleGUI as sg

class TelaPresenca(TelaAbstrata):

  def tela_opcoes(self):
    layout = [
      [sg.Text('PRESENÇA')],
      [sg.Submit(button_text=('Adicionar entrada'), key='1')],
      [sg.Submit(button_text=('Adicionar saída'), key='2')],
      [sg.Submit(button_text=('Retornar'), key='0')],
    ]

    window = sg.Window('Tela presença', element_justification='center').Layout(layout)
    button, values = window.Read()
    window.close()
    return int(button)

  def tela_teste(self):
    layout = [
        [sg.Text('Resultado'), sg.Radio('Negativo', "RADIO1", default=True, key="resultado"), sg.Radio('Positivo', "RADIO1", key="resultado_inverso")],
        [sg.Text('Há quantas horas você fez o teste: '), sg.InputText(key='horas')],
        [sg.Button('Ok')],
    ]
    window = sg.Window('Teste do COVID-19', element_justification='center').Layout(layout)
    button, values = window.Read()
    window.close()
    return values

  def le_num_inteiro(self, mensagem: str = "", inteiros_validos=None):
      return super().le_num_inteiro(mensagem, inteiros_validos)
    
  def seleciona_pessoa(self):
    layout = [
        [sg.Text('Nome'), sg.InputText(key='nome')],
        [sg.Button('Buscar')],
    ]
    window = sg.Window('Seleciona pessoa', element_justification='center').Layout(layout)
    a, values = window.Read()
    window.close()
    print (values='nome'),
    return values
