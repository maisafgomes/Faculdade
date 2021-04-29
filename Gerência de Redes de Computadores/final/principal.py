import conexoesTCP
import conexoesUDP
import PySimpleGUI as sg

sg.theme('dark purple 4')

layout_main = [[sg.Text('Digite IP')],
                [sg.Input()],
               [sg.Button("TCP", key='1'),
                sg.Button("UDP", key='2'),
                sg.Button("TCP e UDP", key='3')
                ]]



window_main = sg.Window('Trabalho 3 OGCR 30/03/2021 Maísa Gomes',
                            layout_main,
                            font='Arial 16',
                            element_justification="center",
                            auto_size_buttons=True,
                            auto_size_text=True)

while True:
    event, values = window_main.read()
    if event == '1':
       conexoesTCP.buscaConexoesTCP(values[0])
       conexoesTCP.buscaConexoesTCP2(values[0])
    elif event == '2':
        conexoesUDP.buscaConexoesUDP(values[0])
    elif event == '3':
        conexoesTCP.buscaConexoesTCP(values[0])
        conexoesTCP.buscaConexoesTCP2(values[0])
        conexoesUDP.buscaConexoesUDP(values[0])

    elif event is None:
            break
