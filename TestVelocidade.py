from PySimpleGUI.PySimpleGUI import Button
import speedtest
import PySimpleGUI as sg

def Painel():
    Fdownload = 0
    Fupload = 0

    while True:

        saida = [
            [sg.Text(f'Download: {Fdownload}\nUpload: {Fupload}', size=(50, 0), justification='center', font=50)],
        ]
        
        layout = [
                [sg.Frame(f'', saida)],
                [sg.Button('Iniciar', size=(15,2), key='_iniciar_'), sg.Button('Sair', key='_sair_', size=(10,2))]
        ]

        window = sg.Window('Teste de Velociadade', layout, element_justification='center', size=(350,150))
        event, values = window.read()

        if event == sg.WIN_CLOSED or event == '_sair_':
            break
            window.close()

        elif event == '_iniciar_':

            app = speedtest.Speedtest()

            download = app.download()
            RSdownload = round(download)
            Fdownload = int(RSdownload / 1e+6)

            upload = app.upload()
            RSupload = round(upload)
            Fupload = int(RSupload / 1e+6)

            print(Fdownload, Fupload)
            window.close()

Painel()